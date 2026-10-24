# Arara: referências, pose sobre verde e recortes

Textos e requests preservados do experimento. Os grafos e metadados dos PNGs acompanham as saídas quando disponíveis. Referências GPT fornecidas separadamente como frente e lateral.

## prompts.json

```json
{
  "tool": "built-in image_gen",
  "design": "An original anthropomorphic green-winged macaw adventurer character, upright bipedal bird with natural bird anatomy and feathered wings used as arms. Scarlet-red head, neck, breast and upper wing shoulders; broad saturated leaf-green middle wing feather bands; saturated royal-blue outer flight feathers and long blue-and-red tail; white bare face patches with fine red feather lines, pale ivory hooked upper beak, dark lower beak, expressive dark eyes, gray scaled feet with claws. A small tan leather cross-body satchel, no other clothing. The green bands are broad visible parts of both wings, including exposed feather edges. Clean stylized 2D animation character art, crisp dark linework, flat cel shading, consistent proportions.",
  "front": "Create a single FRONT VIEW character reference image, full body, upright neutral standing pose, both wings slightly away from body so feather bands are visible, long tail visible behind legs. An original anthropomorphic green-winged macaw adventurer character, upright bipedal bird with natural bird anatomy and feathered wings used as arms. Scarlet-red head, neck, breast and upper wing shoulders; broad saturated leaf-green middle wing feather bands; saturated royal-blue outer flight feathers and long blue-and-red tail; white bare face patches with fine red feather lines, pale ivory hooked upper beak, dark lower beak, expressive dark eyes, gray scaled feet with claws. A small tan leather cross-body satchel, no other clothing. The green bands are broad visible parts of both wings, including exposed feather edges. Clean stylized 2D animation character art, crisp dark linework, flat cel shading, consistent proportions. Plain solid black background. Entire character including crest, wingtips, tail and feet visible with generous margin. One character, one view only, no labels, no text, no ground shadow. Portrait canvas.",
  "side": {
    "references": [
      "front.png"
    ],
    "prompt": "Using the input front reference, create the same character in a single true LEFT SIDE PROFILE VIEW, facing image left. Preserve its exact character design, proportions, feather color placement and satchel. An original anthropomorphic green-winged macaw adventurer character, upright bipedal bird with natural bird anatomy and feathered wings used as arms. Scarlet-red head, neck, breast and upper wing shoulders; broad saturated leaf-green middle wing feather bands; saturated royal-blue outer flight feathers and long blue-and-red tail; white bare face patches with fine red feather lines, pale ivory hooked upper beak, dark lower beak, expressive dark eyes, gray scaled feet with claws. A small tan leather cross-body satchel, no other clothing. The green bands are broad visible parts of both wings, including exposed feather edges. Clean stylized 2D animation character art, crisp dark linework, flat cel shading, consistent proportions. Full body, neutral standing with wing relaxed slightly away from torso so green and blue feather bands are readable, beak profile, long tail and both feet completely visible. One character, one view only. Solid black background, generous margin, no labels, no text, no ground shadow. Portrait canvas."
  },
  "pose": {
    "references": [
      "front.png",
      "side.png"
    ]
  }
}

```