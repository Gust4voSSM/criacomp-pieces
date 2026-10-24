"""Reuse the prior RGB/alpha Canny analysis across current and earlier results."""
from pathlib import Path
import csv
import hashlib
import json
import sys
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, PngImagePlugin

ROOT=Path(__file__).resolve().parent
ZERO_RGB='--zero-transparent-rgb' in sys.argv
OUT=ROOT/('mask-comparison-zero-rgb' if ZERO_RGB else 'mask-comparison-all')
OUT.mkdir(exist_ok=True)
SIZE=(768,1152)
BASE=ROOT/'gpt-charsheets-original-prompts'
CASES=[
 ('Atual: falando','current',BASE/'modal-concat-run/results/vn_qwen/sprite_speaking_rgba_00001_.png'),
 ('Atual: ouvindo','current',BASE/'modal-concat-run/results/vn_qwen/sprite_listening_rgba_00001_.png'),
 ('Atual: refletindo','current',BASE/'modal-concat-run/results/vn_qwen/sprite_thinking_rgba_00001_.png'),
 ('Anterior: falando','previous',BASE/'modal-results/vn_qwen/sprite_speaking_rgba_00001_.png'),
 ('Anterior: ouvindo','previous',BASE/'modal-results/vn_qwen/sprite_listening_rgba_00001_.png'),
 ('Anterior: refletindo','previous',BASE/'modal-results/vn_qwen/sprite_thinking_rgba_00001_.png'),
 ('FLUX + BiRefNet','baseline',ROOT/'flux2-aceno-alpha/source-sprite_00001_.png'),
 ('FLUX + mascara GPT','baseline',ROOT/'flux2-aceno-alpha/flux2-generated-mask-rgba.png'),
 ('GPT RGB primeiro','baseline',ROOT/'pose-from-refs/pose-rgba.png'),
 ('GPT mascara primeiro','baseline',ROOT/'mask-first/pose-rgba.png'),
 ('Qwen Spaces','baseline',ROOT/'flux2-aceno-alpha/qwen-spaces-native.png'),
 ('Qwen Modal seed 12345','baseline',ROOT/'flux2-aceno-alpha/qwen-native-seed12345.png'),
]
FONT=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',18)
SMALL=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',14)

def measure(original):
    # Same independent per-channel Lanczos and Canny thresholds as compare_rgb_alpha.py.
    im=Image.merge('RGBA',[c.resize(SIZE,Image.Resampling.LANCZOS) for c in original.split()])
    arr=np.array(im);rgb,a=arr[:,:,:3],arr[:,:,3]
    binary=(a>=128).astype('uint8')
    boundary=binary-cv2.erode(binary,np.ones((3,3),np.uint8))
    near=cv2.dilate(boundary,np.ones((9,9),np.uint8))>0
    results={}
    for low,high in [(30,80),(60,160),(100,200)]:
        edges=np.maximum.reduce([cv2.Canny(rgb[:,:,i].copy(),low,high) for i in range(3)])
        dist=cv2.distanceTransform((edges==0).astype('uint8'),cv2.DIST_L2,cv2.DIST_MASK_PRECISE)
        values=dist[boundary>0]
        results[f'canny_{low}_{high}']={'mean_distance_px':float(values.mean()),
            'p95_distance_px':float(np.percentile(values,95)),
            'within_1px_pct':float((values<=1).mean()*100),
            'within_2px_pct':float((values<=2).mean()*100)}
        if low==60: main=edges
    overlay=(rgb.astype(float)*.6).astype('uint8')
    overlay[(main>0)&near]=[0,255,255];overlay[boundary>0]=[255,0,255]
    # Native-alpha residual statistics, same distant-background definition as prior analysis.
    na=np.array(original.getchannel('A'))
    expanded=cv2.dilate((na>=128).astype('uint8'),np.ones((31,31),np.uint8))>0
    background=na[~expanded]
    stats={'native_alpha_min':int(na.min()),'native_alpha_max':int(na.max()),
        'native_background_alpha_mean_0_255':float(background.mean()),
        'native_background_nonzero_pct':float((background>0).mean()*100)}
    return im,Image.fromarray(overlay),results,stats

def composite(im,color):
    return Image.alpha_composite(Image.new('RGBA',im.size,color),im).convert('RGB')

rows=[];assets=[]
for label,group,path in CASES:
    source=Image.open(path)
    im=source.convert('RGBA')
    cleaning={}
    if ZERO_RGB:
        array=np.array(im)
        before=array.copy()
        transparent=array[:,:,3]==0
        changed=transparent&np.any(array[:,:,:3]!=0,axis=2)
        array[:,:,:3][transparent]=0
        assert np.array_equal(array[:,:,3],before[:,:,3])
        assert np.array_equal(array[:,:,:3][~transparent],before[:,:,:3][~transparent])
        clean=OUT/'cleaned'/group/path.parent.parent.name
        clean.mkdir(parents=True,exist_ok=True)
        # A source-path digest avoids collisions between experiments with identical PNG names.
        clean=clean/(hashlib.sha256(str(path).encode()).hexdigest()[:8]+'-'+path.name)
        info=PngImagePlugin.PngInfo()
        for key,value in source.info.items():
            if isinstance(value,str): info.add_text(key,value)
        info.add_text('rgb_cleanup','RGB zeroed only where alpha equals zero; alpha and all alpha>0 RGB pixels preserved.')
        Image.fromarray(array).save(clean,pnginfo=info)
        im=Image.open(clean).convert('RGBA')
        assert np.array_equal(np.array(im),array)
        cleaning={'cleaned_path':str(clean),'zero_alpha_pixels':int(transparent.sum()),
                  'changed_rgb_pixels':int(changed.sum()),'alpha_unchanged':True,
                  'all_nonzero_alpha_rgb_unchanged':True}
    normalized,overlay,result,stats=measure(im)
    row={'label':label,'group':group,'path':str(path),'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
         'native_size':list(im.size),'analysis_size':list(SIZE),'alignment':result,**stats,**cleaning}
    # Visual previews resize premultiplied RGBA via Pillow, avoiding hidden-RGB bleed.
    rows.append(row);assets.append((label,group,im.resize(SIZE,Image.Resampling.LANCZOS),overlay))
    print(label,round(result['canny_60_160']['within_1px_pct'],2),round(result['canny_60_160']['mean_distance_px'],3),flush=True)

# Three rows per page keep all native comparisons readable.
for start in range(0,len(assets),3):
    page=Image.new('RGB',(5*256,3*426),'#eeeeee');draw=ImageDraw.Draw(page)
    for row,(label,group,im,overlay) in enumerate(assets[start:start+3]):
        yy,xx=np.indices((im.height,im.width));check=np.where(((xx//18+yy//18)%2)[...,None],190,240).astype('uint8')
        checker=Image.fromarray(np.repeat(check,3,axis=-1)).convert('RGBA')
        panels=[('Branco',composite(im,'white')),('Escuro',composite(im,'#101a2c')),
                ('Xadrez',Image.alpha_composite(checker,im).convert('RGB')),
                ('Alpha',im.getchannel('A').convert('RGB')),('RGB x A',overlay)]
        for col,(title,panel) in enumerate(panels):
            page.paste(panel.resize((256,384),Image.Resampling.LANCZOS),(col*256,row*426+42))
            draw.text((col*256+6,row*426+4),label,font=SMALL,fill='black')
            draw.text((col*256+6,row*426+23),title,font=SMALL,fill='black')
    page.save(OUT/f'page-{start//3+1:02}.png')

# Actual native 3x enlargements of current hand regions on white/dark, without smoothing.
detail=Image.new('RGB',(1080,3*400),'#eeeeee');draw=ImageDraw.Draw(detail)
boxes={'Atual: falando':(105,370,270,490),'Atual: ouvindo':(140,540,280,670),'Atual: refletindo':(345,145,485,275)}
for row,(label,_,path) in enumerate(CASES[:3]):
    entry=rows[row]
    native=Image.open(entry.get('cleaned_path',path)).convert('RGBA');box=boxes[label]
    for col,(title,panel) in enumerate([('Branco',composite(native,'white')),('Escuro',composite(native,'#101a2c')),('Alpha',native.getchannel('A').convert('RGB'))]):
        crop=panel.crop(box)
        crop=crop.resize((crop.width*2,crop.height*2),Image.Resampling.NEAREST)
        detail.paste(crop,(col*360+(350-crop.width)//2,row*400+45))
        draw.text((col*360+6,row*400+8),label+' / '+title,font=FONT,fill='black')
detail.save(OUT/'current-hands.png')
provenance=ROOT/'flux2-aceno-alpha/compare_rgb_alpha.py'
(OUT/'metrics.json').write_text(json.dumps({'method_source':str(provenance),
    'method_source_sha256':hashlib.sha256(provenance.read_bytes()).hexdigest(),'results':rows},indent=2),encoding='utf-8')
with (OUT/'metrics.csv').open('w',newline='',encoding='utf-8-sig') as f:
    writer=csv.writer(f);writer.writerow(['version','within_1px_pct','within_2px_pct','mean_distance_px','p95_distance_px','background_alpha_mean_0_255'])
    for r in rows:
        m=r['alignment']['canny_60_160'];writer.writerow([r['label'],m['within_1px_pct'],m['within_2px_pct'],m['mean_distance_px'],m['p95_distance_px'],r['native_background_alpha_mean_0_255']])
