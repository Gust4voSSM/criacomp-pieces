# Qwen: primeiras três poses com referências GPT

Textos e requests preservados do experimento. Os grafos e metadados dos PNGs acompanham as saídas quando disponíveis. Referências GPT fornecidas separadamente como frente e lateral.

## Textos preservados em request-workflow.json

```json
[
  {
    "title": "Shared prefix",
    "text": [
      "This is an RGBA image with transparency."
    ]
  },
  {
    "title": "Shared character",
    "text": [
      "a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform"
    ]
  },
  {
    "title": "Shared framing",
    "text": [
      "Full body, entire character visible with margin around head, hands and feet."
    ]
  },
  {
    "title": "Shared style",
    "text": [
      "Visual novel character illustration, anime style, flat anime cel shading, clean crisp lineart, soft even studio lighting."
    ]
  },
  {
    "title": "Shared constraints",
    "text": [
      "No scenery, no floor shadow, no text, no border."
    ]
  },
  {
    "title": "Shared suffix",
    "text": [
      "The image has alpha channel and the background is transparent."
    ]
  },
  {
    "title": "Exact prompt - speaking",
    "text": [
      "This is an RGBA image with transparency. Use image 1 as the front character reference and image 2 as the side character reference. Create one visual novel dialogue sprite of exactly the same character, preserving her face, silver side ponytail, ribbon, navy sailor uniform, white neck scarf, gold emblems, pleated skirt, dark thigh-high stockings and black shoes. Full body, standing upright facing the viewer, head level, both feet resting naturally, entire hair and shoes inside the frame. She is speaking calmly with a small friendly smile and her mouth slightly open. One forearm is gently bent with an open palm near waist level in a restrained conversational gesture; the other arm hangs relaxed. Keep the gesture close to the body. Match the reference art style and proportions. One character and one view only. The image has an alpha channel and the background is transparent."
    ]
  },
  {
    "title": "Exact prompt - listening",
    "text": [
      "This is an RGBA image with transparency. Use image 1 as the front character reference and image 2 as the side character reference. Create one visual novel dialogue sprite of exactly the same character, preserving her face, silver side ponytail, ribbon, navy sailor uniform, white neck scarf, gold emblems, pleated skirt, dark thigh-high stockings and black shoes. Full body, standing upright facing the viewer, head level, both feet resting naturally, entire hair and shoes inside the frame. She is listening attentively, with a calm neutral expression, relaxed eyebrows, eyes directed toward the viewer and mouth closed. Both arms rest naturally beside the body, hands relaxed with fingers together, shoulders at ease. Match the reference art style and proportions. One character and one view only. The image has an alpha channel and the background is transparent."
    ]
  },
  {
    "title": "Exact prompt - thinking",
    "text": [
      "This is an RGBA image with transparency. Use image 1 as the front character reference and image 2 as the side character reference. Create one visual novel dialogue sprite of exactly the same character, preserving her face, silver side ponytail, ribbon, navy sailor uniform, white neck scarf, gold emblems, pleated skirt, dark thigh-high stockings and black shoes. Full body, standing upright facing the viewer, head level, both feet resting naturally, entire hair and shoes inside the frame. She is considering what to say, with a thoughtful expression, mouth closed, eyebrows slightly drawn together and gaze gently shifted to one side. One hand rests lightly beneath her chin, with fingers naturally curled; the other arm rests beside her body. Keep the gesture restrained and close to the torso. Match the reference art style and proportions. One character and one view only. The image has an alpha channel and the background is transparent."
    ]
  }
]
```