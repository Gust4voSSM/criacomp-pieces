import importlib.util
import json
import zipfile
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
destination = (ROOT/'results').resolve()
with zipfile.ZipFile(ROOT/'results.zip') as archive:
    for entry in archive.infolist():
        if not (destination/entry.filename).resolve().is_relative_to(destination):
            raise ValueError('Unsafe archive path')
    archive.extractall(destination)
request = json.loads((ROOT/'submitted-request.json').read_text(encoding='utf-8-sig'))
summary = json.loads((destination/'summary.json').read_text(encoding='utf-8'))
assert len(summary['images']) == 1
record = summary['images'][0]
sprite = Image.open(destination/record['file'])
graph = json.loads(sprite.info['prompt'])
workflow = json.loads(sprite.info['workflow'])
inputs = next(n['inputs'] for n in graph.values() if n['class_type']=='VNQwenPrompt')
values = {k:graph[str(v[0])]['inputs']['text'] if isinstance(v,list) else v for k,v in inputs.items()}
assert values['action'] == request['poses'][0]['prompt']
assert values['character'] == ''
assert values['prefix'] == 'This is an RGBA image with transparency.'
assert values['suffix'] == '<image1> shows the front view of the character. <image2> shows the side view of the same character, wearing the same outfit. The image has alpha channel and the background is transparent.'
sampler = next(n['inputs'] for n in graph.values() if n['class_type']=='KSampler')
assert (sampler['seed'],sampler['steps'],sampler['cfg'],sampler['denoise']) == (12345,40,1.0,1.0)
assert workflow['extra']['vn_qwen']['reference_manifest']['reference_id'] == request['reference_id']
spec = importlib.util.spec_from_file_location('vn_prompt', ROOT.parents[3]/'qwen-modal-update/custom_nodes/vn_qwen/__init__.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
(ROOT/'actual-prompt.txt').write_text(module.VNQwenPrompt().run(**values)[0],encoding='utf-8')
verification = dict(record, seconds=summary['seconds'], exact_action_match=True,
                    identity_description_omitted=True, added_context_intro=False,
                    seed=sampler['seed'], steps=sampler['steps'], cfg=sampler['cfg'])
(ROOT/'verification.json').write_text(json.dumps(verification,indent=2),encoding='utf-8')
preview = Image.new('RGB',(832,654),'white')
for i,(path,label) in enumerate([
    (ROOT.parent/'reference-views-run/results'/record['file'],'Previous pose prompt'),
    (destination/record['file'],'Shorter explaining pose prompt')]):
    thumb=Image.open(path).convert('RGBA')
    thumb.thumbnail((416,624),Image.Resampling.LANCZOS)
    preview.paste(thumb,(416*i+(416-thumb.width)//2,30),thumb)
    ImageDraw.Draw(preview).text((416*i+8,8),label,fill='black')
preview.save(ROOT/'comparison.png')
print(json.dumps(verification,indent=2))
