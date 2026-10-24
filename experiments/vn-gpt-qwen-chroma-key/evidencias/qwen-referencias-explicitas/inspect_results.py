import hashlib
import importlib.util
import json
import zipfile
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parents[3]
destination = (ROOT/'results').resolve()
with zipfile.ZipFile(ROOT/'results.zip') as archive:
    for entry in archive.infolist():
        if not (destination/entry.filename).resolve().is_relative_to(destination):
            raise ValueError('Unsafe archive path')
    archive.extractall(destination)
summary = json.loads((destination/'summary.json').read_text(encoding='utf-8'))
assert len(summary['images']) == 1
row = summary['images'][0]
sprite = Image.open(destination/row['file'])
graph = json.loads(sprite.info['prompt'])
workflow = json.loads(sprite.info['workflow'])
node = next(n['inputs'] for n in graph.values() if n['class_type']=='VNQwenPrompt')
values = {k:graph[str(v[0])]['inputs']['text'] if isinstance(v,list) else v for k,v in node.items()}
spec = importlib.util.spec_from_file_location('vn_prompt', WORKSPACE/'qwen-modal-update/custom_nodes/vn_qwen/__init__.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
actual = module.VNQwenPrompt().run(**values)[0]
assert actual == (ROOT/'expected-prompt.txt').read_text(encoding='utf-8')
assert values['character'] == ''
request = json.loads((ROOT/'submitted-request.json').read_text(encoding='utf-8'))
previous_request = json.loads((ROOT.parent/'two-pose-run/submitted-request.json').read_text(encoding='utf-8-sig'))
assert request['poses'][0] == previous_request['poses'][0]
sampler = next(n['inputs'] for n in graph.values() if n['class_type']=='KSampler')
assert sampler['seed'] == request['poses'][0]['seed']
manifest = workflow['extra']['vn_qwen']['reference_manifest']
assert manifest['reference_id'] == request['reference_id']
assert manifest['description'] not in actual
assert sprite.mode == 'RGBA'
verification = dict(row, seconds=summary['seconds'], seed=sampler['seed'],
                    exact_prompt_match=True, common_identity_omitted=True,
                    action_and_seed_match_previous=True, reference_id=manifest['reference_id'],
                    sha256=hashlib.sha256((destination/row['file']).read_bytes()).hexdigest())
(ROOT/'verification.json').write_text(json.dumps(verification, indent=2), encoding='utf-8')
(ROOT/'actual-prompt.txt').write_text(actual, encoding='utf-8')
preview = Image.new('RGB', (832, 654), 'white')
for i, (path, label) in enumerate([
    (ROOT.parent/'two-pose-run/results'/row['file'], 'Previous: common identity description'),
    (destination/row['file'], 'New: reference-view sentences, no identity prose')]):
    thumb = Image.open(path).convert('RGBA')
    thumb.thumbnail((416,624), Image.Resampling.LANCZOS)
    preview.paste(thumb, (416*i+(416-thumb.width)//2,30), thumb)
    ImageDraw.Draw(preview).text((416*i+6,8), label, fill='black')
preview.save(ROOT/'comparison.png')
print(json.dumps(verification, indent=2))
