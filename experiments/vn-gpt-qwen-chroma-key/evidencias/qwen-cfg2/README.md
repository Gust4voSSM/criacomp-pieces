# CFG 2 and negative-prompt control

Completed exactly two new images of the same speaking pose, using the existing parallel reference-only flow. No positive prompt edits, no additional context introduction, and no common identity description.

| Condition | Job | Runner seconds |
| --- | --- | --- |
| CFG 2, empty negative | `fc-01M5NMRF4DTF2H8EW58CPZFBVV` | 91.329 |
| CFG 2, sourced negative | `fc-01M5NMRHC4V1PM5BG326PCBHH6` | 87.494 |

Both are native RGBA 832 x 1248, alpha range 0–255, seed 12345, 40 steps, Euler/simple, denoise 1. PNG metadata verifies exact positive-prompt agreement with the prior CFG 1 baseline, the same reference ID, and identical graph nodes except sampler CFG and encoder negative text. See `verification.json`.

`comparison.png`: prior CFG 1 baseline, CFG 2 blank-negative control, CFG 2 sourced-negative treatment, from left to right. `hands-detail.png` shows native-scale hand/torso crops of the two CFG 2 results. Preview compositing/resizing does not alter the original sprites in each condition's `results/vn_qwen/` folder.

## Visual assessment

Both CFG 2 images have a more coherent hand-at-hip gesture than the prior CFG 1 result. The control also shows a clearer three-quarter stance. Adding the sourced negatives changes the hand shapes slightly and returns the lower body toward a frontal stance, but does not demonstrate an unambiguous further hand-anatomy improvement over the CFG 2 control. Fine finger anatomy remains stylized and should be reviewed at actual display size.

The clearest improvement in this pair is consistent with raising CFG, since the blank-negative control already improves. The negative list's additional benefit is inconclusive for this seed. This is one controlled subject/seed comparison, not proof of general reliability or a guarantee that the broad negative list is optimal.

See `SOURCES.md` for empirical evidence quality and source limitations. The original API remains unchanged; optional guidance controls are available only on the parallel flow. All 15 local regression tests passed before deployment.
