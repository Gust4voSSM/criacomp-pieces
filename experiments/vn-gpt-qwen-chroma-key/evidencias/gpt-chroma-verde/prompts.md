# GPT: três poses sobre verde e chroma key

Textos e requests preservados do experimento. Os grafos e metadados dos PNGs acompanham as saídas quando disponíveis. Referências GPT fornecidas separadamente como frente e lateral.

## prompts-completos.json

```json
{
  "tool": "built-in image_gen",
  "references": [
    "D:\\gugu9\\Documents\\Faculdade\\9o_Periodo\\Criacomp\\Projeto Ferramenta\\output\\imagegen\\gpt-charsheets-original-prompts\\front.png",
    "D:\\gugu9\\Documents\\Faculdade\\9o_Periodo\\Criacomp\\Projeto Ferramenta\\output\\imagegen\\gpt-charsheets-original-prompts\\side.png"
  ],
  "prompts": {
    "speaking": "Use Image 1 as the front character identity reference and Image 2 as the side character identity reference. Create one single portrait full-body image of the same character, preserving her design, face, hair and outfit.\nThis is an RGB image with a solid chroma-key green background. a young woman with long silver hair in a side ponytail tied with a navy ribbon, violet eyes, wearing a navy-blue sailor school uniform with a white neck scarf and gold emblems, pleated skirt, dark thigh-high stockings and black loafers. gentle friendly smiling expression, mouth slightly open, one hand open near waist in a conversational gesture, other arm relaxed, front view, standing pose. Full body, entire character visible with margin around head, hands and feet. Visual novel character illustration, anime style, flat anime cel shading, clean crisp lineart, soft even studio lighting. No scenery, no floor shadow, no text, no border. The entire background is uniform pure bright green (#00FF00), including gaps between limbs and hair. No background gradients or texture. Keep green background color off the character.",
    "listening": "Use Image 1 as the front character identity reference and Image 2 as the side character identity reference. Create one single portrait full-body image of the same character, preserving her design, face, hair and outfit.\nThis is an RGB image with a solid chroma-key green background. a young woman with long silver hair in a side ponytail tied with a navy ribbon, violet eyes, wearing a navy-blue sailor school uniform with a white neck scarf and gold emblems, pleated skirt, dark thigh-high stockings and black loafers. calm attentive expression, mouth closed, arms relaxed at sides, looking at the viewer, front view, standing pose. Full body, entire character visible with margin around head, hands and feet. Visual novel character illustration, anime style, flat anime cel shading, clean crisp lineart, soft even studio lighting. No scenery, no floor shadow, no text, no border. The entire background is uniform pure bright green (#00FF00), including gaps between limbs and hair. No background gradients or texture. Keep green background color off the character.",
    "thinking": "Use Image 1 as the front character identity reference and Image 2 as the side character identity reference. Create one single portrait full-body image of the same character, preserving her design, face, hair and outfit.\nThis is an RGB image with a solid chroma-key green background. a young woman with long silver hair in a side ponytail tied with a navy ribbon, violet eyes, wearing a navy-blue sailor school uniform with a white neck scarf and gold emblems, pleated skirt, dark thigh-high stockings and black loafers. thoughtful pensive expression, mouth closed, one hand resting under chin, gaze slightly averted, front view, standing pose. Full body, entire character visible with margin around head, hands and feet. Visual novel character illustration, anime style, flat anime cel shading, clean crisp lineart, soft even studio lighting. No scenery, no floor shadow, no text, no border. The entire background is uniform pure bright green (#00FF00), including gaps between limbs and hair. No background gradients or texture. Keep green background color off the character."
  },
  "thinking_prompt_provenance": "Prompt exato recuperado da chamada imageGeneration no chat Compare green-screen pose masks; adicionado ao arquivo que continha apenas speaking e listening."
}
```

## prompts.json

```json
{
  "tool": "built-in image_gen",
  "references": [
    "D:\\gugu9\\Documents\\Faculdade\\9o_Periodo\\Criacomp\\Projeto Ferramenta\\output\\imagegen\\gpt-charsheets-original-prompts\\front.png",
    "D:\\gugu9\\Documents\\Faculdade\\9o_Periodo\\Criacomp\\Projeto Ferramenta\\output\\imagegen\\gpt-charsheets-original-prompts\\side.png"
  ],
  "prompts": {
    "speaking": "Use Image 1 as the front character identity reference and Image 2 as the side character identity reference. Create one single portrait full-body image of the same character, preserving her design, face, hair and outfit.\nThis is an RGB image with a solid chroma-key green background. a young woman with long silver hair in a side ponytail tied with a navy ribbon, violet eyes, wearing a navy-blue sailor school uniform with a white neck scarf and gold emblems, pleated skirt, dark thigh-high stockings and black loafers. gentle friendly smiling expression, mouth slightly open, one hand open near waist in a conversational gesture, other arm relaxed, front view, standing pose. Full body, entire character visible with margin around head, hands and feet. Visual novel character illustration, anime style, flat anime cel shading, clean crisp lineart, soft even studio lighting. No scenery, no floor shadow, no text, no border. The entire background is uniform pure bright green (#00FF00), including gaps between limbs and hair. No background gradients or texture. Keep green background color off the character.",
    "listening": "Use Image 1 as the front character identity reference and Image 2 as the side character identity reference. Create one single portrait full-body image of the same character, preserving her design, face, hair and outfit.\nThis is an RGB image with a solid chroma-key green background. a young woman with long silver hair in a side ponytail tied with a navy ribbon, violet eyes, wearing a navy-blue sailor school uniform with a white neck scarf and gold emblems, pleated skirt, dark thigh-high stockings and black loafers. calm attentive expression, mouth closed, arms relaxed at sides, looking at the viewer, front view, standing pose. Full body, entire character visible with margin around head, hands and feet. Visual novel character illustration, anime style, flat anime cel shading, clean crisp lineart, soft even studio lighting. No scenery, no floor shadow, no text, no border. The entire background is uniform pure bright green (#00FF00), including gaps between limbs and hair. No background gradients or texture. Keep green background color off the character."
  }
}

```