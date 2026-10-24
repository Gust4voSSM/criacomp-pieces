# Macaw magenta key experiment

Generated one new greeting pose using built-in image_gen with the same separate front and side references and pose description as the green test. Background instruction changed to flat #FF00FF. Raw output is pose-magenta.png, opaque RGB at 1024 x 1536. Exact prompt and reference paths: prompt.json. No API call, explicit model selection or seed control. Artwork and pose vary slightly between generations, so this is not a registered background-only comparison.

## Finding

Switching the background color alone is insufficient: the old Euclidean distance key leaves a conspicuous magenta fringe. A magenta-specific alpha combined with foreground color recovery is visibly cleaner in inspected feather-edge crops on white and dark backgrounds. Green feather interiors remain opaque instead of being removed or desaturated. This is a promising result for this character, not a general-purpose quality guarantee or proof every edge is perfect.

The candidate is well separated from the character's red, green and blue feathers: magenta has both red and blue above green. This allows a magenta-excess measure min(R-G,B-G) without broadly removing any of the character's three main hues. A character with real magenta/purple highlights would require a collision check before applying it.

## Sampling and keying

Four 32 x 32 corner patches yield median RGB values (251,4,248), (251,4,248), (250,4,248), (251,3,248). Their componentwise median is (251,4,248); maximum Euclidean deviation is 1. Corner disagreement greater than 20 is rejected. This check is procedural but does not prove the corners are semantically background in every future input.

Alpha = 1 - clip((min(R-G,B-G)-8)/(screen_excess-16),0,1), where screen_excess=min(Bg.R-Bg.G,Bg.B-Bg.G). The foreground RGB is recovered using F=(C-(1-alpha)*Bg)/alpha, clipped to byte range. RGB is zero where quantized alpha is zero. No erosion, hole filling, interior recoloring or hand-painted mask is used. Recovery changes partially transparent RGB to subtract the screen contribution. It is an estimated RGB compositing model, not a recovered ground-truth foreground.

The old distance baseline uses the same 8..80 Euclidean RGB distance transition as the green experiment. Both its magenta result and the improved result are retained. The raw-alpha variant keeps RGB unchanged at nonzero alpha, isolating the effect of background color recovery.

## Diagnostics

The previous OpenCV measure() function is reused directly by AST extraction: 768 x 1152 analysis, independent channel Lanczos resizing, alpha >=128 internal boundary, Canny per RGB channel with thresholds 30/80, 60/160, 100/200, Euclidean edge distance. Main 60/160 diagnostic: green distance 99.92% within 1px; magenta distance 99.93%; magenta unmix 99.96%. These nearly equal scores conceal large visible fringe differences and should not decide acceptance. Background residual alpha is also recorded in metrics.json; tiny nonzero background pixels remain.

## Files

- pose-magenta.png: untouched generation.
- pose-recovered-rgba.png: preferred experimental transparent result; pose-recovered-mask.png: alpha.
- recovered-white.png / recovered-dark.png: native-size composites.
- pose-distance-rgba.png: previous distance method on magenta.
- pose-raw-alpha-rgba.png: magenta alpha without foreground RGB recovery.
- comparison.png: full characters on white/dark, alpha and edge diagnostics.
- edge-detail.png: 2x nearest-neighbor feather crops; the green and magenta artwork is not registered.
- fringe-comparison.png: dark-background edge crops for green distance, magenta distance, magenta unmix.
- key_magenta.py: reproducible implementation; metrics.json: results; prompt.json: exact generation prompt.

Reproduce: python output/imagegen/macaw-magenta-key-study/key_magenta.py
