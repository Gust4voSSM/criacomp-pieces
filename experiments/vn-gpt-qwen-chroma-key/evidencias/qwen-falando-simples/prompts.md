# Qwen: gesto de fala simplificado

Textos e requests preservados do experimento. Os grafos e metadados dos PNGs acompanham as saídas quando disponíveis. Referências GPT fornecidas separadamente como frente e lateral.

## actual-prompt.txt

```text
This is an RGBA image with transparency. Pose her calmly explaining something, with both feet planted and her torso in a shallow three-quarter turn. Raise one bent forearm beside her torso, palm facing upward with fingers loosely together. Rest the other hand against her hip. Keep her head facing the viewer, with a friendly expression and mouth slightly open. Full body, entire character visible with margin around head, hands and feet. Visual novel character illustration, anime style, flat anime cel shading, clean crisp lineart, soft even studio lighting. No scenery, no floor shadow, no text, no border. <image1> shows the front view of the character. <image2> shows the side view of the same character, wearing the same outfit. The image has alpha channel and the background is transparent.
```

## submitted-request.json

```json
{
  "poses": [
    {
      "name": "speaking",
      "seed": 12345,
      "prompt": "Pose her calmly explaining something, with both feet planted and her torso in a shallow three-quarter turn. Raise one bent forearm beside her torso, palm facing upward with fingers loosely together. Rest the other hand against her hip. Keep her head facing the viewer, with a friendly expression and mouth slightly open."
    }
  ],
  "reference_id": "61d2bfbcb43206a635023a5660305255a124e0db635ab23f22cae012d4f3a24e"
}

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
      ""
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
      "<image1> shows the front view of the character. <image2> shows the side view of the same character, wearing the same outfit. The image has alpha channel and the background is transparent."
    ]
  }
]
```