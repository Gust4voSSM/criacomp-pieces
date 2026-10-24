"""Chroma-key experiment; reuse existing OpenCV measure() without running its report."""
from pathlib import Path
import ast, hashlib, json
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
PRIOR = ROOT.parent / 'compare_all_masks.py'
SIZE = (768, 1152)
tree = ast.parse(PRIOR.read_text(encoding='utf-8-sig'))
fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'measure')
exec(compile(ast.Module(body=[fn], type_ignores=[]), str(PRIOR), 'exec'))
FONT = ImageFont.truetype('C:/Windows/Fonts/arial.ttf', 17)

def comp(im, bg):
    return Image.alpha_composite(Image.new('RGBA', im.size, bg), im).convert('RGB')

def key(rgb):
    arr = np.array(rgb).astype(np.float32)
    border = np.concatenate([arr[:8].reshape(-1,3), arr[-8:].reshape(-1,3), arr[:,:8].reshape(-1,3), arr[:,-8:].reshape(-1,3)])
    screen = np.median(border, axis=0)
    excess = arr[:,:,1] - np.maximum(arr[:,:,0], arr[:,:,2])
    screen_excess = float(screen[1] - max(screen[0], screen[2]))
    if screen_excess < 100:
        raise ValueError(f'Background is not a strong green screen: {screen}')
    # Fixed thresholds for all three poses. No erosion, hole fill or per-pose tuning.
    alpha = 1 - np.clip((excess - 8) / (screen_excess - 16), 0, 1)
    a8 = np.rint(alpha * 255).astype(np.uint8)
    # Invert C = alpha*F + (1-alpha)*screen, then remove remaining green spill.
    foreground = (arr - (1-alpha[:,:,None])*screen) / np.maximum(alpha[:,:,None], 1/255)
    foreground = np.clip(foreground, 0, 255)
    fringe = (alpha > 0) & (alpha < 1)
    foreground[:,:,1][fringe] = np.minimum(foreground[:,:,1][fringe], np.maximum(foreground[:,:,0], foreground[:,:,2])[fringe])
    foreground[a8 == 0] = 0
    soft = Image.fromarray(np.dstack([np.rint(foreground).astype(np.uint8), a8]))
    hsv = cv2.cvtColor(np.array(rgb), cv2.COLOR_RGB2HSV)
    green = cv2.inRange(hsv, (35,70,40), (90,255,255))
    hard = Image.fromarray(np.dstack([np.array(rgb), 255-green]))
    return soft, hard, a8, screen.tolist()

rows = []
for pose in ['speaking','listening','thinking']:
    rgb = Image.open(ROOT/f'{pose}-green.png').convert('RGB')
    soft, hard, alpha, screen = key(rgb)
    soft.save(ROOT/f'{pose}-rgba.png')
    hard.save(ROOT/f'{pose}-hard-rgba.png')
    Image.fromarray(alpha).save(ROOT/f'{pose}-mask.png')
    variants = [('Green soft', soft), ('Green hard HSV', hard)]
    for label, folder in [('Previous concat', 'modal-concat-run/results'), ('Previous first', 'modal-results')]:
        variants.append((label, Image.open(ROOT.parent/'gpt-charsheets-original-prompts'/folder/'vn_qwen'/f'sprite_{pose}_rgba_00001_.png').convert('RGBA')))
    sheet = Image.new('RGB', (5*256, len(variants)*426), '#eeeeee')
    draw = ImageDraw.Draw(sheet)
    for row, (label, im) in enumerate(variants):
        normalized, overlay, measurements, stats = measure(im)
        # Also repeat the prior zero-invisible-RGB condition for every method.
        clean = np.array(im); clean[:,:,:3][clean[:,:,3]==0] = 0
        _, _, zero_measurements, _ = measure(Image.fromarray(clean))
        entry = {'pose':pose, 'variant':label, 'native_size':list(im.size), 'alignment':measurements, 'zero_rgb_alignment':zero_measurements, **stats}
        if label.startswith('Green'): entry['sampled_screen_rgb'] = screen
        rows.append(entry)
        preview = im.resize(SIZE, Image.Resampling.LANCZOS)
        panels = [('White',comp(preview,'white')), ('Dark',comp(preview,'#101a2c')), ('Alpha',preview.getchannel('A').convert('RGB')), ('RGB ignored alpha',normalized.convert('RGB')), ('RGB vs alpha',overlay)]
        for col, (title, panel) in enumerate(panels):
            x,y = col*256,row*426
            sheet.paste(panel.resize((256,384),Image.Resampling.LANCZOS),(x,y+42))
            draw.text((x+5,y+3),pose+' / '+label,font=FONT,fill='black')
            draw.text((x+5,y+22),title,font=FONT,fill='black')
    sheet.save(ROOT/f'compare-{pose}.png')
    # Native nearest-neighbor head/hair and hands/torso crops for visual inspection.
    w,h=soft.size
    boxes=[(int(.27*w),0,int(.78*w),int(.39*h)),(int(.17*w),int(.12*h),int(.83*w),int(.54*h))]
    detail=Image.new('RGB',(1200,900),'#eeeeee'); dd=ImageDraw.Draw(detail)
    for row,box in enumerate(boxes):
        for col,(name,panel) in enumerate([('White',comp(soft,'white')),('Dark',comp(soft,'#101a2c')),('Mask',soft.getchannel('A').convert('RGB'))]):
            crop=panel.crop(box); crop.thumbnail((395,410),Image.Resampling.NEAREST)
            detail.paste(crop,(col*400,row*450+35)); dd.text((col*400+5,row*450+5),pose+' / '+name,font=FONT,fill='black')
    detail.save(ROOT/f'details-{pose}.png')

(ROOT/'metrics.json').write_text(json.dumps({'method_source':str(PRIOR),'method_sha256':hashlib.sha256(PRIOR.read_bytes()).hexdigest(),'analysis_size':SIZE,'key_settings':{'excess_offset':8,'screen_tolerance':8,'hard_hsv_lower':[35,70,40],'hard_hsv_upper':[90,255,255]},'results':rows},indent=2),encoding='utf-8')
with (ROOT/'metrics.csv').open('w',encoding='utf-8') as f:
    f.write('pose,variant,within_1px_pct,mean_distance_px,zero_rgb_within_1px_pct\n')
    for r in rows:
        m=r['alignment']['canny_60_160']; z=r['zero_rgb_alignment']['canny_60_160']
        line=f"{r['pose']},{r['variant']},{m['within_1px_pct']:.4f},{m['mean_distance_px']:.4f},{z['within_1px_pct']:.4f}"
        print(line);f.write(line+'\n')

overview = Image.new('RGB',(3*320,3*520),'#eeeeee'); od=ImageDraw.Draw(overview)
for col,pose in enumerate(['speaking','listening','thinking']):
    im=Image.open(ROOT/f'{pose}-rgba.png').convert('RGBA')
    for row,(label,panel) in enumerate([('White',comp(im,'white')),('Dark',comp(im,'#101a2c')),('Mask',im.getchannel('A').convert('RGB'))]):
        panel.thumbnail((320,480),Image.Resampling.LANCZOS)
        overview.paste(panel,(col*320,row*520+35));od.text((col*320+5,row*520+5),pose+' / '+label,font=FONT,fill='black')
overview.save(ROOT/'overview.png')

prior_rows=json.loads((ROOT.parent/'mask-comparison-all/metrics.json').read_text())['results']
report=['# GPT green background / chroma-key experiment','',
'Generated with built-in image_gen from the separate GPT front.png and side.png references, one call per pose. No selectable exact model version or seed is exposed by that tool. All three raw outputs are 1024 x 1536; sprites and masks retain native dimensions.', '',
'The three pose descriptions and character/style/framing text were retained from vn-final-concatenated-prompts.txt. Transparency instructions were replaced by solid green instructions, and explicit input-reference roles were added. Exact submitted prompts and reference paths are in prompts.json. This is a GPT RGB + keying versus Qwen native RGBA comparison; the generator, resolution and artwork differ, so it does not isolate background color alone.','',
'## Results','',
'Soft key gives usable cutouts, with finger gaps and main hair gaps preserved in the inspected previews. It does not consistently improve alignment over the latest Qwen run. Thin hair strands retain some tint/halo on white or dark backgrounds. The hard HSV variant keeps more green edge contamination and has binary alpha; the soft key has smoother transitions. Thinking has the weakest soft-key alignment. Its averted gaze is clearer, but the free arm is crossed rather than lowered, which was not constrained in the prompt. No manual retouching was applied.','',
'| Pose | Green soft <=1px | Mean px | Green hard <=1px | Latest Qwen <=1px | Earlier Qwen <=1px |','|---|---:|---:|---:|---:|---:|']
for pose in ['speaking','listening','thinking']:
    rr={r['variant']:r['alignment']['canny_60_160'] for r in rows if r['pose']==pose}
    report.append(f"| {pose} | {rr['Green soft']['within_1px_pct']:.2f}% | {rr['Green soft']['mean_distance_px']:.3f} | {rr['Green hard HSV']['within_1px_pct']:.2f}% | {rr['Previous concat']['within_1px_pct']:.2f}% | {rr['Previous first']['within_1px_pct']:.2f}% |")
report+=['','## Method and limits','',
'The existing measure() function is loaded directly from ../compare_all_masks.py via AST, without executing or changing the previous report. Identical analysis size 768 x 1152, independent Lanczos resizing per channel, RGB-channel Canny thresholds 30/80, 60/160 and 100/200, alpha >=128 internal contour, and Euclidean distance transform. Main table uses 60/160. Every previous pose was measured again. metrics.json also includes the zero-invisible-RGB condition for all variants. Soft outputs already have RGB zero at A=0.','',
'Soft key uses green excess G-max(R,B), a median border screen color, an 8-level foreground offset and 8-level screen tolerance. It recovers foreground color with the sampled screen, clamps residual green excess on partially transparent pixels, and zeros RGB at alpha=0. Hard key uses cv2.inRange in HSV, lower (35,70,40), upper (90,255,255). Same settings for all poses, no erosion/dilation/filling in keying. Background is visibly green but not mathematically constant #00FF00, so the screen is sampled per image.','',
'These are edge-coincidence diagnostics, not segmentation accuracy: no reference masks exist. Key alpha is derived from RGB, and RGB is subsequently decontaminated, so the scores are coupled. The previous zero-RGB experiment already demonstrated that hidden RGB affects this metric without changing alpha. High score cannot certify missing strands, green spill, anatomy, or pose compliance.','',
'## Other prior baselines (saved original-RGB diagnostics)','',
'These are copied from the prior saved metrics, not rerun in this experiment. They use the same nominal OpenCV settings but different artwork.','',
'| Baseline | <=1px | Mean px |','|---|---:|---:|']
for r in prior_rows:
    if r['group']=='baseline':
        m=r['alignment']['canny_60_160'];report.append(f"| {r['label']} | {m['within_1px_pct']:.2f}% | {m['mean_distance_px']:.3f} |")
report+=['','## Files','',
'- *-green.png: untouched generated RGB originals.','- *-rgba.png: soft-key transparent sprites; *-mask.png: grayscale alpha masks.','- *-hard-rgba.png: basic HSV baseline, retained for comparison.','- overview.png: three poses on white, dark and alpha.','- compare-*.png: soft key, hard key, latest Qwen, earlier Qwen; white/dark/mask/RGB/edge-overlay columns.','- details-*.png: head/hair and upper-body crops.','- prompts.json: exact submitted prompts; metrics.json and metrics.csv: measurements.','',
'Reproduce: python output/imagegen/gpt-green-key-study/analyze.py','']
(ROOT/'README.md').write_text('\n'.join(report),encoding='utf-8')
