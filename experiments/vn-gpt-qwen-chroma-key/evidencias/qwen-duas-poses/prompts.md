# Qwen: poses mais distintas

Textos e requests preservados do experimento. Os grafos e metadados dos PNGs acompanham as saídas quando disponíveis. Referências GPT fornecidas separadamente como frente e lateral.

## submitted-request.json

```json
{
  "poses": [
    {
      "name": "speaking",
      "seed": 12345,
      "prompt": "Shift her weight onto one leg with the opposite knee relaxed, moving the hips slightly toward screen-right. Turn the torso gently toward screen-left while keeping the face directed toward the viewer. Lean forward a little as if inviting a response. Extend one forearm toward screen-left at lower-chest height with the palm open upward and a clear gap between elbow and waist. Bend the other arm with its hand resting lightly at her waist. Give the shoulders a gentle opposing tilt to the hips. Friendly engaged smile, mouth slightly open, eyes on the viewer."
    },
    {
      "name": "thinking",
      "seed": 34567,
      "prompt": "Shift the weight onto one leg and turn the torso to a shallow three-quarter angle toward screen-left. Turn the head back toward the viewer so both eyes remain visible, then direct the gaze slightly upward toward screen-right. Bend one arm across the upper waist to support the opposite elbow; raise that forearm with the fingertips resting lightly beneath the chin. Keep the two bent arms readable as a compact triangular shape. Let one shoulder sit slightly higher than the other. Reflective expression, gently drawn brows, closed mouth."
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