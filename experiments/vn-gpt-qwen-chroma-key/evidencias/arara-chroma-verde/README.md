# Green-winged macaw: references, pose and green-key experiment

Generated with built-in image_gen, three calls: front by text; side using front; greeting pose using both separate references. Exact prompts and reference roles are in prompts.json. No API call, exact model selection or seed control was used. All raw generated images are opaque RGB, 1024 x 1536. Raw files are preserved as front.png, side.png and pose-green.png.

## Finding

This example CAN be keyed on bright green because the character's leaf-green feathers are darker and sufficiently separated from the actual screen. It is not evidence that every red/green/blue design forces an RGBA-model fallback. It DOES expose failures in our previous broad green keyers.

- The previous soft green-excess key makes real green feathers translucent and suppresses their green channel during despill, changing their colors.
- The previous HSV range key removes most of the green feather areas outright.
- An additional experimental screen-distance key preserves these green areas much better, including feather shapes in the inspected views. Some fine green fringe remains along the silhouette, so the output is not a certified perfect matte.

The sampled screen median is RGB (3, 250, 2), rather than the requested (0, 255, 0). Background sampling reuses the previous eight-pixel border estimator, not a new robust clustering implementation.

In a manually inspected 30 x 30 interior patch of green feathers, box (270,510,300,540), the original mean RGB is approximately (78.3,161.3,37.1). The mean resulting alpha is:

| Key | Mean alpha / 255 |
|---|---:|
| Previous soft green-excess | 172.33 |
| Previous broad HSV | 2.83 |
| Screen-distance variant | 255.00 |

This patch is an illustrative foreground check, not an automatically segmented ground-truth mask or a whole-character quality score.

## Methods

The old key() function is loaded unchanged from ../gpt-green-key-study/analyze.py via AST. The prior OpenCV measure() function is similarly loaded unchanged from ../compare_all_masks.py. All three Canny thresholds are executed at analysis size 768 x 1152, with independent channel Lanczos resampling, alpha >=128 internal boundary and Euclidean edge distance. No previous files were edited.

The additional screen-distance method uses Euclidean RGB distance to the sampled screen: alpha=clip((distance-8)/72,0,1), transparent at distance <=8, opaque at distance >=80. It recovers foreground RGB using the sampled screen and estimated alpha; RGB is zero at alpha=0. No broad green despill is applied, because that would alter the character's real green feathers. These are experimental fixed thresholds for this test, not a calibrated automatic acceptance rule.

| Key | Boundary within 1px of RGB edge | Mean distance |
|---|---:|---:|
| Previous soft | 99.61% | 0.301px |
| Previous HSV | 99.88% | 0.184px |
| Screen distance | 99.92% | 0.392px |

The destructive HSV key still scores 99.88%. This demonstrates why the edge score cannot validate foreground preservation. All masks depend on the RGB, and RGB recovery further couples these diagnostics. No segmentation accuracy is claimed.

## Outputs

- front.png, side.png: character references on black.
- pose-green.png: untouched generated greeting pose.
- pose-soft-rgba.png and pose-hard-rgba.png: previous keyers, retained as failed comparisons.
- pose-distance-rgba.png: better experimental cutout; pose-distance-mask.png: its alpha.
- comparison.png: three keyers, original/white/dark/alpha/edge-overlay columns.
- wing-detail.png: enlarged feather comparison; distance-white.png and distance-dark.png: full-size compositions.
- metrics.json: all measurements and source-code hashes; prompts.json: exact prompt set.

Reproduce from the workspace root: python output/imagegen/macaw-green-key-study/analyze.py
