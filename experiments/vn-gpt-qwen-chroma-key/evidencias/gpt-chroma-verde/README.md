# GPT green background / chroma-key experiment

Generated with built-in image_gen from the separate GPT front.png and side.png references, one call per pose. No selectable exact model version or seed is exposed by that tool. All three raw outputs are 1024 x 1536; sprites and masks retain native dimensions.

The three pose descriptions and character/style/framing text were retained from vn-final-concatenated-prompts.txt. Transparency instructions were replaced by solid green instructions, and explicit input-reference roles were added. Exact submitted prompts and reference paths are in prompts.json. This is a GPT RGB + keying versus Qwen native RGBA comparison; the generator, resolution and artwork differ, so it does not isolate background color alone.

## Results

Soft key gives usable cutouts, with finger gaps and main hair gaps preserved in the inspected previews. It does not consistently improve alignment over the latest Qwen run. Thin hair strands retain some tint/halo on white or dark backgrounds. The hard HSV variant keeps more green edge contamination and has binary alpha; the soft key has smoother transitions. Thinking has the weakest soft-key alignment. Its averted gaze is clearer, but the free arm is crossed rather than lowered, which was not constrained in the prompt. No manual retouching was applied.

| Pose | Green soft <=1px | Mean px | Green hard <=1px | Latest Qwen <=1px | Earlier Qwen <=1px |
|---|---:|---:|---:|---:|---:|
| speaking | 99.15% | 0.291 | 99.65% | 99.60% | 99.37% |
| listening | 99.50% | 0.294 | 99.63% | 99.10% | 99.22% |
| thinking | 98.60% | 0.392 | 98.49% | 99.80% | 99.64% |

## Method and limits

The existing measure() function is loaded directly from ../compare_all_masks.py via AST, without executing or changing the previous report. Identical analysis size 768 x 1152, independent Lanczos resizing per channel, RGB-channel Canny thresholds 30/80, 60/160 and 100/200, alpha >=128 internal contour, and Euclidean distance transform. Main table uses 60/160. Every previous pose was measured again. metrics.json also includes the zero-invisible-RGB condition for all variants. Soft outputs already have RGB zero at A=0.

Soft key uses green excess G-max(R,B), a median border screen color, an 8-level foreground offset and 8-level screen tolerance. It recovers foreground color with the sampled screen, clamps residual green excess on partially transparent pixels, and zeros RGB at alpha=0. Hard key uses cv2.inRange in HSV, lower (35,70,40), upper (90,255,255). Same settings for all poses, no erosion/dilation/filling in keying. Background is visibly green but not mathematically constant #00FF00, so the screen is sampled per image.

These are edge-coincidence diagnostics, not segmentation accuracy: no reference masks exist. Key alpha is derived from RGB, and RGB is subsequently decontaminated, so the scores are coupled. The previous zero-RGB experiment already demonstrated that hidden RGB affects this metric without changing alpha. High score cannot certify missing strands, green spill, anatomy, or pose compliance.

## Other prior baselines (saved original-RGB diagnostics)

These are copied from the prior saved metrics, not rerun in this experiment. They use the same nominal OpenCV settings but different artwork.

| Baseline | <=1px | Mean px |
|---|---:|---:|
| FLUX + BiRefNet | 99.16% | 0.322 |
| FLUX + mascara GPT | 90.56% | 0.585 |
| GPT RGB primeiro | 97.36% | 0.382 |
| GPT mascara primeiro | 71.23% | 1.060 |
| Qwen Spaces | 98.93% | 0.436 |
| Qwen Modal seed 12345 | 99.67% | 0.534 |

## Files

- *-green.png: untouched generated RGB originals.
- *-rgba.png: soft-key transparent sprites; *-mask.png: grayscale alpha masks.
- *-hard-rgba.png: basic HSV baseline, retained for comparison.
- overview.png: three poses on white, dark and alpha.
- compare-*.png: soft key, hard key, latest Qwen, earlier Qwen; white/dark/mask/RGB/edge-overlay columns.
- details-*.png: head/hair and upper-body crops.
- prompts.json: exact submitted prompts; metrics.json and metrics.csv: measurements.

Reproduce: python output/imagegen/gpt-green-key-study/analyze.py
