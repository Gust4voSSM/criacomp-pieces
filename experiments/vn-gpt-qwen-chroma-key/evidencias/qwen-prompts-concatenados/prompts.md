# Qwen: poses com prompts compartilhados

Textos e requests preservados do experimento. Os grafos e metadados dos PNGs acompanham as saídas quando disponíveis. Referências GPT fornecidas separadamente como frente e lateral.

## submitted-request.json

```json
{
  "poses": [
    {
      "name": "speaking",
      "seed": 12345,
      "prompt": "gentle friendly smiling expression, mouth slightly open, one hand open near waist in a conversational gesture, other arm relaxed, front view, standing pose"
    },
    {
      "name": "listening",
      "seed": 23456,
      "prompt": "calm attentive expression, mouth closed, arms relaxed at sides, looking at the viewer, front view, standing pose"
    },
    {
      "name": "thinking",
      "seed": 34567,
      "prompt": "thoughtful pensive expression, mouth closed, one hand resting under chin, gaze slightly averted, front view, standing pose"
    }
  ],
  "reference_id": "61d2bfbcb43206a635023a5660305255a124e0db635ab23f22cae012d4f3a24e"
}
```

## vn-final-concatenated-prompts.txt

```text
speaking
This is an RGBA image with transparency. a young woman with long silver hair in a side ponytail tied with a navy ribbon, violet eyes, wearing a navy-blue sailor school uniform with a white neck scarf and gold emblems, pleated skirt, dark thigh-high stockings and black loafers. gentle friendly smiling expression, mouth slightly open, one hand open near waist in a conversational gesture, other arm relaxed, front view, standing pose. Full body, entire character visible with margin around head, hands and feet. Visual novel character illustration, anime style, flat anime cel shading, clean crisp lineart, soft even studio lighting. No scenery, no floor shadow, no text, no border. The image has alpha channel and the background is transparent.

listening
This is an RGBA image with transparency. a young woman with long silver hair in a side ponytail tied with a navy ribbon, violet eyes, wearing a navy-blue sailor school uniform with a white neck scarf and gold emblems, pleated skirt, dark thigh-high stockings and black loafers. calm attentive expression, mouth closed, arms relaxed at sides, looking at the viewer, front view, standing pose. Full body, entire character visible with margin around head, hands and feet. Visual novel character illustration, anime style, flat anime cel shading, clean crisp lineart, soft even studio lighting. No scenery, no floor shadow, no text, no border. The image has alpha channel and the background is transparent.

thinking
This is an RGBA image with transparency. a young woman with long silver hair in a side ponytail tied with a navy ribbon, violet eyes, wearing a navy-blue sailor school uniform with a white neck scarf and gold emblems, pleated skirt, dark thigh-high stockings and black loafers. thoughtful pensive expression, mouth closed, one hand resting under chin, gaze slightly averted, front view, standing pose. Full body, entire character visible with margin around head, hands and feet. Visual novel character illustration, anime style, flat anime cel shading, clean crisp lineart, soft even studio lighting. No scenery, no floor shadow, no text, no border. The image has alpha channel and the background is transparent.

```

## Textos preservados em results/request-workflow.json

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
      "a young woman with long silver hair in a side ponytail tied with a navy ribbon, violet eyes, wearing a navy-blue sailor school uniform with a white neck scarf and gold emblems, pleated skirt, dark thigh-high stockings and black loafers"
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
  }
]
```