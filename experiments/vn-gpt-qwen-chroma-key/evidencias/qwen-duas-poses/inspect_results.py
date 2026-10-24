import hashlib
import json
import zipfile
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
OLD = ROOT.parents[1] / 'gpt-charsheets-original-prompts' / 'modal-concat-run'
request = json.loads((ROOT / 'submitted-request.json').read_text(encoding='utf-8-sig'))
destination = (ROOT / 'results').resolve()
with zipfile.ZipFile(ROOT / 'results.zip') as archive:
    for entry in archive.infolist():
        target = (destination / entry.filename).resolve()
        if not target.is_relative_to(destination):
            raise ValueError('Unsafe archive path')
    archive.extractall(destination)

summary = json.loads((destination / 'summary.json').read_text(encoding='utf-8'))
assert len(summary['images']) == 2, summary
manifest = json.loads((OLD / 'reference-manifest.json').read_text(encoding='utf-8'))
rows = []
preview = Image.new('RGB', (832, 654), 'white')
comparison = Image.new('RGB', (1664, 654), 'white')
for i, pose in enumerate(request['poses']):
    record = next(r for r in summary['images'] if f"sprite_{pose['name']}_" in r['file'])
    path = destination / record['file']
    sprite = Image.open(path)
    assert sprite.mode == 'RGBA', sprite.mode
    graph = json.loads(sprite.info['prompt'])
    prompt_id, node = next((key, n) for key, n in graph.items()
                           if n['class_type'] == 'VNQwenPrompt' and n['inputs']['action'] == pose['prompt'])
    inputs = node['inputs']
    def value(item):
        if isinstance(item, str):
            return item
        source = graph[str(item[0])]
        return source['inputs']['text']
    assert inputs['action'] == pose['prompt']
    assert value(inputs['character']) == manifest['description']
    encoder_id = next(key for key, n in graph.items() if n['class_type'] == 'TextEncodeQwenImage21'
                      and str(n['inputs']['prompt'][0]) == str(prompt_id))
    sampler = next(n['inputs'] for n in graph.values() if n['class_type'] == 'KSampler'
                   and str(n['inputs']['positive'][0]) == str(encoder_id))
    assert sampler['seed'] == pose['seed']
    rows.append({'name': pose['name'], 'file': record['file'], 'size': list(sprite.size),
                 'mode': sprite.mode, 'alpha_range': list(sprite.getchannel('A').getextrema()),
                 'action_matches_request': True, 'common_description_matches_previous_run': True,
                 'seed': sampler['seed'], 'steps': sampler['steps'], 'cfg': sampler['cfg'],
                 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()})
    def panel(canvas, x, image, label):
        thumb = image.convert('RGBA')
        thumb.thumbnail((416, 624), Image.Resampling.LANCZOS)
        canvas.paste(thumb, (x + (416-thumb.width)//2, 30), thumb)
        ImageDraw.Draw(canvas).text((x+8, 8), label, fill='black')
    panel(preview, i*416, sprite, pose['name'])
    previous = Image.open(OLD / 'results' / record['file'])
    panel(comparison, i*832, previous, pose['name']+' - previous')
    panel(comparison, i*832+416, sprite, pose['name']+' - new')
preview.save(ROOT / 'two-poses.png')
comparison.save(ROOT / 'before-after.png')
(ROOT / 'verification.json').write_text(json.dumps(rows, indent=2), encoding='utf-8')
print(json.dumps({'seconds': summary['seconds'], 'verification': rows}, indent=2))
