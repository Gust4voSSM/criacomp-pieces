# Qwen-Image-2.1: expressive visual novel sprites

Research date: 23 October 2026. Target: existing GPT Image front/side references -> Qwen-Image-2.1 native RGBA workflow in `qwen-modal-update`.

Status: source research and local workflow inspection completed. Prompt proposals below have not been tested through inference. Existing workflow, prompts, and deployed service were not modified.

## Main finding

Preserve character design while deliberately changing the pose geometry. The current results retain almost the same legs, hips, torso orientation, and head position. This makes small redraw differences easy to compare. Stronger acting may make those differences less conspicuous, but it will not repair actual identity or costume drift. That perceptual benefit is a hypothesis to evaluate in a dialogue scene.

The useful target is a sustainable conversational gesture: a posture the character could hold through several lines. More dynamic does not have to mean an action scene.

## What the existing evidence shows

Inspected `gpt-charsheets-original-prompts/modal-concat-run/three-poses.png`, its README, `vn-final-concatenated-prompts.txt`, the short request, and the local graph builder and prompt node.

- Speaking changes one arm and the mouth; listening stays close to the frontal reference; thinking brings a hand to the chin. All three keep a similar upright lower body and nearly frontal torso.
- Every submitted action specifies `front view, standing pose`. Listening explicitly asks for arms relaxed at the sides. The requested changes are small; these outputs do not establish that Qwen cannot produce stronger poses.
- Prompt assembly currently puts a prose character description before the action and never assigns explicit roles to the two references.
- External-reference generation uses an empty output latent and `denoise=1.0`, with two reference images supplied to `TextEncodeQwenImage21`. This is not evidence of a low-denoise img2img setting. Increasing denoise is not an available fix above 1.0.
- External mode fixes 40 steps and CFG 1.0, with an empty negative prompt. Keep that working baseline for the first prompt comparison.
- Earlier local research found a seed collision in another experiment. The latest request already uses separate seeds for speaking, listening, and thinking. That earlier diagnosis should not be assumed to explain these latest poses.

## What Qwen's own guidance supports

**Official:** Qwen's edit prompt enhancer distinguishes modifying an existing picture from composing a new picture of a referenced subject. Its instructions call for explicit reference roles, concrete changes, strong edit execution, and concise identity preservation. It warns that verbose descriptions of preserved appearance can cause regeneration and identity drift. For multiple references it uses `<image1>` and `<image2>`. These are recommendations in the enhancer's instructions, not proof that other wording fails in the image model. [Official edit enhancer](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-I2I/raw/main/system_prompt.txt).

**Official:** Qwen-Image-2.1 supports multiple reference images and native transparency. Retain its recommended RGBA opening and closing sentences. Do not transfer assumptions about older Qwen-Image-Edit checkpoints to this version. [Model card](https://huggingface.co/Qwen/Qwen-Image-2.1).

**Official:** Diffusers documents joint text/image conditioning and order-sensitive reference blocks. It recommends 40 steps without guidance by default. In that pipeline, negative prompting requires CFG above 1. These statements do not establish numerical equivalence with every ComfyUI implementation. [Diffusers documentation](https://huggingface.co/docs/diffusers/main/en/api/pipelines/qwenimage21).

**Proposal for this project:** name both sheets as design sources and explicitly release their posture. Use plain English instructions rather than weighted Stable Diffusion tags. Start with geometry that can be seen: weight-bearing leg, hip shift, torso turn, shoulder line, both arms, head tilt, and gaze. Exact phrasing and reference order still need testing in this runner.

## What makes a useful VN sprite pose

**Practitioner evidence:** the creator of *One Thousand Acts of Decency* builds pose sets around personality and recurring functions such as neutral, shock, and pointing. Reserved and expressive characters get different gesture ranges. [Creator's sprite devlog](https://itch.io/devlog/1575413/devlog-15-creating-sprites.amp).

**Practitioner evidence:** *Of Sense and Soul* treats sprite changes and movement as part of narrative pacing. Its artist also reports that small discrepancies between facial variants became distracting during mouth animation. [Artist's cinematography devlog](https://forsythiaproductions.itch.io/of-sense-and-soul/devlog/480454/sprites-camera-action-vn-cinematography-in-of-sense-and-soul).

**Production example:** *Aaron and The Void* uses posed 3D figures, separates heads for expression variants, and recommends checking sprites in their actual scene. This is one artist's workflow, not a universal requirement or evidence for AI prompting. [Sprite creation process](https://eyematerror.itch.io/aaron-and-the-void/devlog/976396/devlog-my-sprite-creation-process).

The following are design recommendations for this project, not model guarantees:

1. Give every pose a conversational intention. “Invite a response” suggests a different body from “defend a position,” even if both have an open mouth.
2. Make the upper-body silhouette distinct. The dialogue box may hide changes confined to the legs. Elbow spacing, shoulder tilt, lean, and head angle should survive the expected crop.
3. Use asymmetry and a believable center of gravity. Shift weight onto one leg, turn the torso gently, and give the arms different jobs.
4. Keep the face and key costume features readable. Extreme profile, hands across the eyes, and strong foreshortening make routine dialogue harder to read and compare.
5. Let pose affect cloth and hair naturally. Preserving the exact contour of a sleeve or ponytail while turning the body would conflict with the new geometry. Preserve their design and attachment instead.
6. Keep a stable camera, apparent scale, lighting, and foot baseline. Do not demand identical head coordinates when the pose includes a lean or bow. Alignment should preserve natural anatomy.
7. Reserve broad reactions for story beats. Constantly changing the entire pose on every line can create visual noise.

## Suggested pose vocabulary

This is an initial set to adapt to the character's actual personality. The existing friendly expression is not enough evidence to invent a complete personality.

| Function | Body action | Distinctive silhouette | Use |
| --- | --- | --- | --- |
| Attentive / curious | Slight forward lean, inclined head, hands loosely joined at upper waist | Small forward curve and asymmetric shoulders | Listening, inviting elaboration |
| Open / explaining | Weight on one leg, modest torso turn, open palm to the side at chest height | Broad elbow gap and opposing hip/shoulder angles | Speaking, reassuring, offering |
| Reflective / uncertain | Torso angled away, head turned back, one hand at chin, other supporting the elbow | Compact arm triangle and offset head | Considering, doubt, hesitation |
| Confident / teasing | Hip shifted, one hand on hip, other raised in a small gesture | One projecting elbow and tilted shoulder line | Banter, assertion |
| Guarded / skeptical | Torso partly withdrawn, arms folded loosely, chin slightly lowered | Closed upper-body mass | Disbelief, reluctance |
| Embarrassed / apologetic | Slight inward shoulders, inclined head, one hand holding the other forearm | Narrow asymmetric outline | Apology, discomfort |
| Surprised / recoiling | Upper body leans back, elbows bend outward, hands near upper chest | Wider raised-arm contour | Brief reaction beats |
| Greeting / delighted | Small forward lean, one hand raised beside head, other held near waist | High unilateral arm shape | Arrival, recognition, enthusiasm |

“Speaking” and “listening” are dialogue states rather than complete body poses. A guarded character can listen with folded arms or speak with the same folded arms. Think in terms of **body pose + expression + mouth state + gaze**.

For production, a promising approach is several distinct pose bases, each with expressions derived from that accepted base. Ren'Py supports grouped layered-image attributes, but generating separate PNGs does not automatically create aligned compositable layers. [Ren'Py layered images](https://www.renpy.org/doc/html/layeredimage.html).

## Proposed Qwen prompt structure

Use one complete prompt per image. `<image1>` is the front sheet; `<image2>` is the separate side sheet. Keep the uploaded reference order consistent.

```text
This is an RGBA image with transparency.
Create a new full-body visual novel sprite of the character in <image1>.
Use <image1> for facial identity, costume design, colors, and drawing style.
Use <image2> to clarify the same character's side-view construction and hairstyle.
Both images are character-design references. Build a new body pose with a different silhouette from the upright front sheet.
[CONCRETE BODY ACTION, BOTH ARMS, HEAD, GAZE, EXPRESSION]
Preserve the character's identity, proportions, costume details, and rendering style while allowing the hair and clothing to follow the new pose naturally.
Eye-level camera, full body including hands and feet, with clear margins. Match the reference's cel shading and lighting. One character, no scenery, floor shadow, text, or border.
The image has alpha channel and the background is transparent.
```

This template is an untested synthesis. Keep the existing RGBA wording. The exact reference-role paragraph is a prompt instruction, not a hard separation of identity and pose inside the model.

### Action: speaking / inviting

```text
Shift her weight onto one leg with the opposite knee relaxed, moving the hips slightly toward screen-right. Turn the torso gently toward screen-left while keeping the face directed toward the viewer. Lean forward a little as if inviting a response. Extend one forearm toward screen-left at lower-chest height with the palm open upward; keep a clear gap between elbow and waist. Bend the other arm with its hand resting lightly at her waist. Give the shoulders a gentle opposing tilt to the hips. Friendly engaged smile, mouth slightly open, eyes on the viewer.
```

### Action: listening / curious

```text
Stand with the weight on the rear leg and the other foot slightly forward, both feet planted. Angle the torso gently toward screen-right and lean the upper body forward a little in attentive interest. Tilt the head toward screen-left while keeping the eyes on the viewer. Loosely join both hands at the upper waist, with one elbow projecting slightly outward and the other close to the body. Keep the shoulders relaxed and visibly unequal in height. Calm curious expression, slightly raised eyebrows, closed mouth.
```

### Action: thinking / weighing a reply

```text
Shift the weight onto one leg and turn the torso to a shallow three-quarter angle toward screen-left. Turn the head back toward the viewer so both eyes remain visible, then direct the gaze slightly upward toward screen-right. Bend one arm across the upper waist to support the opposite elbow; raise that forearm with the fingertips resting lightly beneath the chin. Keep the two bent arms readable as a compact triangular shape. Let one shoulder sit slightly higher than the other. Reflective expression, gently drawn brows, closed mouth.
```

The adjacent `proposed-three-poses.json` contains action-field versions with reference-role instructions, preserving the existing request schema and seeds. The existing assembler still prepends the uploaded character description; therefore that file tests action changes and reference roles, not the complete operation-first template. A separate future test can compare concise reference anchoring against the current verbose character prefix.

## Minimal evaluation plan

No inference has been run for this study.

1. Compare the three archived prompts against the three proposals with the same references, canvas, settings, and respective seeds. For a strict comparison, rerun both conditions in the same environment; the archived images are a practical visual baseline but may include environment differences.
2. Inspect the body as a silhouette and at the actual VN crop. A changed hand alone should not count as a successful whole-body pose change.
3. Score pose adherence, character identity, costume correctness, anatomy, face visibility, framing, and alpha separately. A different silhouette cannot compensate for a different face.
4. Compare swaps in a short dialogue scene. Check head/foot alignment and whether costume or face details flicker between poses.
5. If the new wording works, verify the strongest pose across a few additional seeds. A single favorable result is not evidence of reliability.
6. If wording is insufficient, test a pose guide as an additional reference with explicit role assignment. A mannequin or owned sketch can specify the silhouette without adding a competing costume or identity. This is an experimental fallback; the current external-reference API accepts exactly two sheets, so it would require an implementation change. An extra reference is not equivalent to a verified ControlNet constraint.

The first experiment should keep the working sampler and RGBA setup. It can answer whether the current limitation is mostly the requested geometry before adding new controls or changing the service.
