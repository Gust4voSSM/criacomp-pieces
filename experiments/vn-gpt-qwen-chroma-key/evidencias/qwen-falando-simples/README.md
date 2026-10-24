# Shorter speaking prompt

Completed one-image job `fc-01M5NMAYCNRF3V6M74FX4KTDTK` on the parallel reference-views API. Same reference pair, seed 12345, 40 steps, CFG 1, Euler/simple, denoise 1. Native RGBA 832 x 1248. Runner time: 68.287 seconds.

The specific action is the previously proposed shorter explaining pose, unchanged. The reference-only flow has no added context introduction or common appearance description. The view labels remain immediately before the transparency postfix. PNG metadata confirms the action, prompt structure, reference ID, and settings; see `verification.json` and `actual-prompt.txt`.

Visual assessment: both feet are now planted, the open palm is raised beside the torso, and the other hand is at the hip. The requested three-quarter torso turn is weak, and the hand at the hip has awkward finger contours. This sample follows the intended grounded stance better than the preceding speaking result, but is not anatomically clean throughout.

Original: `results/vn_qwen/sprite_speaking_rgba_00001_.png`. `comparison.png` shows the previous reference-only experiment on the left and this shorter prompt on the right. Original images were not resized; the comparison is a resized preview. The standard API remains unchanged.
