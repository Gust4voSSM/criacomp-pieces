"""Compare the previous distance key with a magenta-specific alpha and unmixing."""
from pathlib import Path
import ast,json
import cv2
import numpy as np
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parent
SIZE=(768,1152)
source=ROOT.parent/'compare_all_masks.py'
fn=next(n for n in ast.parse(source.read_text(encoding='utf-8-sig')).body if isinstance(n,ast.FunctionDef) and n.name=='measure')
exec(compile(ast.Module(body=[fn],type_ignores=[]),str(source),'exec'))
FONT=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',18)

def comp(im,color):
    return Image.alpha_composite(Image.new('RGBA',im.size,color),im).convert('RGB')

rgb=Image.open(ROOT/'pose-magenta.png').convert('RGB')
c=np.array(rgb).astype(np.float32)
patches=[c[:32,:32],c[:32,-32:],c[-32:,:32],c[-32:,-32:]]
medians=np.array([np.median(p.reshape(-1,3),axis=0) for p in patches])
bg=np.median(medians,axis=0)
if np.linalg.norm(medians-bg,axis=1).max()>20:
    raise ValueError('Corner patches disagree; background estimation rejected')
screen_excess=min(bg[0]-bg[1],bg[2]-bg[1])
if screen_excess<120:raise ValueError('Background is not strong magenta')
# min(R-G,B-G) responds to magenta, while leaving saturated red/blue/green intact.
excess=np.minimum(c[:,:,0]-c[:,:,1],c[:,:,2]-c[:,:,1])
a=1-np.clip((excess-8)/(screen_excess-16),0,1)
da=np.clip((np.linalg.norm(c-bg,axis=2)-8)/72,0,1)

def rgba(alpha,unmix):
    out=c.copy()
    if unmix:out=np.clip((c-(1-alpha[:,:,None])*bg)/np.maximum(alpha[:,:,None],1/255),0,255)
    a8=np.rint(alpha*255).astype(np.uint8);out[a8==0]=0
    return Image.fromarray(np.dstack([np.rint(out).astype(np.uint8),a8]))

distance=rgba(da,True);raw=rgba(a,False);recovered=rgba(a,True)
for name,im in [('distance',distance),('raw-alpha',raw),('recovered',recovered)]:
    im.save(ROOT/f'pose-{name}-rgba.png');im.getchannel('A').save(ROOT/f'pose-{name}-mask.png')
    comp(im,'white').save(ROOT/f'{name}-white.png');comp(im,'#101a2c').save(ROOT/f'{name}-dark.png')
green=Image.open(ROOT.parent/'macaw-green-key-study/pose-distance-rgba.png').convert('RGBA')
variants=[('Green distance',green),('Magenta distance',distance),('Magenta unmix',recovered)]
sheet=Image.new('RGB',(1200,3*485),'#eeeeee');draw=ImageDraw.Draw(sheet);metrics={}
for row,(name,im) in enumerate(variants):
    _,over,m,stats=measure(im);metrics[name]={'alignment':m,**stats}
    for col,(title,panel) in enumerate([('White',comp(im,'white')),('Dark',comp(im,'#101a2c')),('Alpha',im.getchannel('A').convert('RGB')),('Edges',over)]):
        panel=panel.copy();panel.thumbnail((300,450),Image.Resampling.LANCZOS)
        sheet.paste(panel,(col*300,row*485+35));draw.text((col*300+5,row*485+5),name+' / '+title,font=FONT,fill='black')
sheet.save(ROOT/'comparison.png')
detail=Image.new('RGB',(1080,3*410),'#eeeeee');dd=ImageDraw.Draw(detail)
for row,(name,im,box) in enumerate([('Green distance',green,(90,510,270,690)),('Magenta distance',distance,(60,540,240,720)),('Magenta unmix',recovered,(60,540,240,720))]):
    for col,(label,panel) in enumerate([('White',comp(im,'white')),('Dark',comp(im,'#101a2c')),('Alpha',im.getchannel('A').convert('RGB'))]):
        detail.paste(panel.crop(box).resize((360,360),Image.Resampling.NEAREST),(col*360,row*410+40))
        dd.text((col*360+5,row*410+5),name+' / '+label,font=FONT,fill='black')
detail.save(ROOT/'edge-detail.png')
report={'corner_patch_medians_rgb':medians.tolist(),'sampled_background_rgb':bg.tolist(),'max_corner_deviation_rgb':float(np.linalg.norm(medians-bg,axis=1).max()),'alpha_method':'1-clip((min(R-G,B-G)-8)/(screen_excess-16),0,1)','unmix':'F=(C-(1-alpha)*B)/alpha; clip RGB; zero RGB at A=0','results':metrics}
(ROOT/'metrics.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
