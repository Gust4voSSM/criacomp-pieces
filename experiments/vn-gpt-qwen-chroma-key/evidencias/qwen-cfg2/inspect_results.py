import hashlib
import importlib.util
import json
from pathlib import Path
import zipfile
from PIL import Image,ImageDraw

ROOT=Path(__file__).resolve().parent
baseline=ROOT.parent/'speaking-simple-run/results/vn_qwen/sprite_speaking_rgba_00001_.png'
baseline_image=Image.open(baseline)
baseline_graph=json.loads(baseline_image.info['prompt'])
spec=importlib.util.spec_from_file_location('vn_prompt',ROOT.parents[3]/'qwen-modal-update/custom_nodes/vn_qwen/__init__.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
def positive(graph):
    inputs=next(n['inputs'] for n in graph.values() if n['class_type']=='VNQwenPrompt')
    values={k:graph[str(v[0])]['inputs']['text'] if isinstance(v,list) else v for k,v in inputs.items()}
    return module.VNQwenPrompt().run(**values)[0]

panels=[(baseline_image,'CFG 1 / no negative')]
verification=[]
for label in ('control','negative'):
    folder=ROOT/label
    if not (folder/'results.zip').exists():
        print(label,'not downloaded yet')
        continue
    destination=(folder/'results').resolve()
    with zipfile.ZipFile(folder/'results.zip') as archive:
        for entry in archive.infolist():
            if not (destination/entry.filename).resolve().is_relative_to(destination):
                raise ValueError('Unsafe archive path')
        archive.extractall(destination)
    summary=json.loads((destination/'summary.json').read_text())
    assert len(summary['images'])==1
    record=summary['images'][0]
    path=destination/record['file']
    sprite=Image.open(path)
    graph=json.loads(sprite.info['prompt'])
    request=json.loads((folder/'submitted-request.json').read_text())
    assert positive(graph)==positive(baseline_graph)
    for ident,node in graph.items():
        expected=json.loads(json.dumps(baseline_graph[ident]))
        if node['class_type']=='KSampler':
            expected['inputs']['cfg']=2.0
        elif node['class_type']=='TextEncodeQwenImage21':
            expected['inputs']['negative_prompt']=request['negative_prompt']
        assert node==expected,(label,ident)
    workflow=json.loads(sprite.info['workflow'])
    assert workflow['extra']['vn_qwen']['reference_manifest']['reference_id']==request['reference_id']
    assert sprite.mode=='RGBA' and sprite.size==baseline_image.size
    (folder/'actual-positive-prompt.txt').write_text(positive(graph),encoding='utf-8')
    verification.append(dict(label=label,**record,seconds=summary['seconds'],cfg=2,seed=12345,
                             exact_positive_match=True,only_cfg_and_negative_nodes_changed=True,
                             negative_prompt=request['negative_prompt'],sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
    panels.append((sprite,'CFG 2 / '+('empty negative (control)' if label=='control' else 'sourced negative')))
preview=Image.new('RGB',(416*len(panels),654),'white')
for i,(sprite,label) in enumerate(panels):
    thumb=sprite.convert('RGBA')
    thumb.thumbnail((416,624),Image.Resampling.LANCZOS)
    preview.paste(thumb,(416*i+(416-thumb.width)//2,30),thumb)
    ImageDraw.Draw(preview).text((416*i+8,8),label,fill='black')
preview.save(ROOT/'comparison.png')
(ROOT/'verification.json').write_text(json.dumps(verification,indent=2),encoding='utf-8')
print(json.dumps(verification,indent=2))
