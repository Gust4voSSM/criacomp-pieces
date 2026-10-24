# Evidence and test design

Research date: 23 October 2026.

## Selected negative prompt

Source: Anthony Clicheroux's first-hand Qwen-Image-2.1 guide, https://stablediffusion.fr/guide/qwen-image-2-1 . The exact list is preserved in `negative/submitted-request.json`.

The author reports fixed-seed comparisons on illustrated subjects and a general anatomy/artifact negative list. Their preferred configuration also uses CFG 3, APG, and FreSca. It does not isolate the negative list's effect and does not demonstrate hand repair for our reference-based sprites. We use its list unchanged, at the user's requested CFG 2, without adding those patches.

## Closer task, weaker inspectable evidence

https://github.com/pjStyle/qwen_image_2.1_testing reports character pose/expression trials using one reference, seed 42 and 40 steps, with several selected CFG 2 positive/negative pairs. Its README acknowledges no separately rendered application baseline and no evidence of generalization. Linked raw reports/results were not retrievable during this research, so its reported ratings are not independently verified and its exact selected negative pairs were not used here.

## Implementation guidance

https://github.com/Comfy-Org/docs/blob/main/tutorials/image/qwen/qwen-image-2-1.mdx explains that CFG 1 skips the negative branch, and warns that CFG 2 can over-sharpen edges. It recommends fixed-seed comparisons. This supports enabling the negative branch, not any particular negative text.

## Our matched comparison

Existing baseline: `../speaking-simple-run`, CFG 1 and blank negative.

New control: CFG 2 and blank negative. New treatment: CFG 2 and the sourced negative list. Both use exactly the same short speaking prompt, reference pair, seed 12345, canvas, model, 40 steps, Euler/simple, denoise 1 and reference-only concatenation. No identity prose or context introduction is added.

The two new jobs isolate negative text at CFG 2. Comparing control with the archived baseline estimates the effect of raising CFG in this environment. One seed is a controlled case study, not a general reliability estimate. PNG metadata is checked against the baseline graph, allowing only sampler CFG and encoder negative text to differ.
