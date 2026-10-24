"""Run the existing green key unchanged on the macaw stress test."""
from pathlib import Path
import ast, hashlib, json
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT=Path(__file__).resolve().parent
SIZE=(768,1152)
sources={'key':ROOT.parent/'gpt-green-key-study/analyze.py','measure':ROOT.parent/'compare_all_masks.py'}
for name,path in sources.items():
    tree=ast.parse(path.read_text(encoding='utf-8-sig'))
    fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name==name)
    exec(compile(ast.Module(body=[fn],type_ignores=[]),str(path),'exec'))

def comp(im,color):
    return Image.alpha_composite(Image.new('RGBA',im.size,color),im).convert('RGB')

rgb=Image.open(ROOT/'pose-green.png').convert('RGB')
soft,hard,alpha,screen=key(rgb)
soft.save(ROOT/'pose-soft-rgba.png');hard.save(ROOT/'pose-hard-rgba.png')
Image.fromarray(alpha).save(ROOT/'pose-soft-mask.png')
hard.getchannel('A').save(ROOT/'pose-hard-mask.png')
# Additional exploratory key: distance to this specific screen color, not all greens.
# Fixed transition: transparent at <=8 RGB units, opaque at >=80 RGB units.
arr=np.array(rgb).astype(np.float32);bg=np.array(screen,np.float32)
distance=np.linalg.norm(arr-bg,axis=2)
da=np.clip((distance-8)/72,0,1)
da8=np.rint(da*255).astype(np.uint8)
recovered=np.clip((arr-(1-da[:,:,None])*bg)/np.maximum(da[:,:,None],1/255),0,255)
recovered[da8==0]=0
tight=Image.fromarray(np.dstack([np.rint(recovered).astype(np.uint8),da8]))
tight.save(ROOT/'pose-distance-rgba.png');tight.getchannel('A').save(ROOT/'pose-distance-mask.png')
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',18)
sheet=Image.new('RGB',(5*300,3*485),'#eeeeee');draw=ImageDraw.Draw(sheet)
metrics={}
for row,(label,im) in enumerate([('Soft key',soft),('Hard HSV key',hard),('Screen distance',tight)]):
    _,overlay,m,stats=measure(im)
    metrics[label]={'alignment':m,**stats}
    panels=[('Original green',rgb),('White',comp(im,'white')),('Dark',comp(im,'#101a2c')),('Alpha',im.getchannel('A').convert('RGB')),('RGB vs alpha',overlay)]
    for col,(title,panel) in enumerate(panels):
        panel=panel.copy();panel.thumbnail((300,450),Image.Resampling.LANCZOS)
        sheet.paste(panel,(col*300,row*485+35));draw.text((col*300+5,row*485+5),label+' / '+title,font=font,fill='black')
sheet.save(ROOT/'comparison.png')
patch=(270,510,300,540) # Manually inspected interior green-feather patch; not a full ground-truth mask.
patch_stats={}
for label,im in [('Soft key',soft),('Hard HSV key',hard),('Screen distance',tight)]:
    aa=np.array(im.getchannel('A').crop(patch))
    patch_stats[label]={'mean_alpha':float(aa.mean()),'zero_alpha_pct':float((aa==0).mean()*100)}
detail=Image.new('RGB',(4*340,550),'#eeeeee');dd=ImageDraw.Draw(detail)
cropbox=(160,420,420,800)
for col,(label,im) in enumerate([('Original',rgb),('Old soft',comp(soft,'white')),('Old HSV',comp(hard,'white')),('Screen distance',comp(tight,'white'))]):
    crop=im.crop(cropbox);crop=crop.resize((340,497),Image.Resampling.NEAREST)
    detail.paste(crop,(col*340,40));dd.text((col*340+5,8),label,font=font,fill='black')
detail.save(ROOT/'wing-detail.png')
for label,im in [('soft',soft),('hard',hard),('distance',tight)]:
    comp(im,'white').save(ROOT/f'{label}-white.png')
    comp(im,'#101a2c').save(ROOT/f'{label}-dark.png')
(ROOT/'metrics.json').write_text(json.dumps({'sampled_background_rgb':screen,'native_size':rgb.size,'screen_distance_settings':{'transparent_distance':8,'opaque_distance':80,'space':'Euclidean RGB'},'manual_green_feather_patch':{'box':patch,'original_mean_rgb':np.array(rgb.crop(patch)).mean((0,1)).tolist(),'results':patch_stats},'method_sources':{k:{'path':str(v),'sha256':hashlib.sha256(v.read_bytes()).hexdigest()} for k,v in sources.items()},'results':metrics},indent=2),encoding='utf-8')
print(json.dumps({'background':screen,'alignment':metrics},indent=2))
