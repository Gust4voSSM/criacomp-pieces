# Parallel reference-views experiment: single speaking pose

Completed job: `fc-01M5NKPHYQXNPDBVSVSJY0W02G`. Exactly one generated image. Runner time: 70.310 seconds. RGBA 832 x 1248, alpha 0–255. Same speaking action, seed 12345, reference pair, 40 steps, CFG 1, Euler/simple, and denoise 1 as the earlier two-pose run.

The tested prompt omits the common identity description and inserts the user's front/side reference sentences immediately before the transparency postfix. See `actual-prompt.txt`. PNG metadata was checked against `expected-prompt.txt` byte for byte, including action and shared prompt fields. The stored reference manifest still contains its original description, but that description is not in the image prompt. See `verification.json`.

Original image: `results/vn_qwen/sprite_speaking_rgba_00001_.png`. Full returned artifacts: `results.zip`. `comparison.png` shows the prior result on the left and this experiment on the right. Only the preview was resized.

Visual assessment: the character remains recognizable and the new leg position differs, but the leg is still lifted and the hands remain awkward. This sample does not establish an improvement from omitting identity prose and labeling views, and cannot isolate those two changes from each other.

## Later correction, not tested through inference

After submission, the user requested introducing the referenced subject before the imperative action. The parallel flow was updated to add `Pose the character shown in the reference images as follows.` immediately after the RGBA prefix. The user explicitly requested no rerun. This archive and its prompt files preserve the actual earlier test, without that new introduction. Future graph and prompt snapshots have `future-` prefixes.

The original production flow was not redeployed or changed. The separate reference-views API reuses its GPU runner with a parallel graph builder.
