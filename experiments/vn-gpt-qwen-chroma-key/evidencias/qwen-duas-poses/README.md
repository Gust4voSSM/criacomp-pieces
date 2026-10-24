# Two stronger VN poses: completed

Job: `fc-01M5NFPCXG62AVWVTGP697FSAK`. Existing references: `61d2bfbcb43206a635023a5660305255a124e0db635ab23f22cae012d4f3a24e`.

Exactly two images generated with the existing deployed Qwen-Image-2.1 API. The request contains only the reference ID, names, seeds, and specific pose instructions; common character, framing, style, and transparency text were concatenated server-side. No deployment or shared prompt changes.

Both outputs are native RGBA, 832 x 1248, alpha range 0–255. Reported runner duration: 94.316 seconds. Settings: 40 steps, CFG 1; speaking seed 12345, thinking seed 34567, matching the earlier respective poses.

PNG generation metadata confirms both requested action strings and the unchanged uploaded common identity description. See `verification.json`. Original files are in `results/vn_qwen/`; `results.zip` preserves the returned archive. Only preview composites were resized.

## Visual inspection

- Speaking has a visibly turned torso, shifted hips, open-palm gesture, and a second bent arm. Qwen also lifted and bent one leg more strongly than the requested relaxed knee. This produces a distinct, playful silhouette, but may be too animated for routine dialogue.
- Thinking has a clear three-quarter torso, tilted head, hand near the chin, and the other forearm crossing the waist. The supporting-elbow relationship and upward averted gaze were not followed precisely; the gaze stays close to the viewer.
- Character design and general rendering remain recognizable in the comparison. This is a visual assessment, not a guarantee of exact face, costume, or edge consistency.
- The results demonstrate that stronger pose instructions can change the silhouette while retaining the working common description. This one pair does not establish reliability across seeds or prove that pose variation eliminates perceptible identity drift.

`two-poses.png` shows the new outputs on white. `before-after.png` places each previous pose beside its new counterpart at the same preview scale.
