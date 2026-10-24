# Qwen: frente e lateral explícitas no prompt

Textos e requests preservados do experimento. Os grafos e metadados dos PNGs acompanham as saídas quando disponíveis. Referências GPT fornecidas separadamente como frente e lateral.

## actual-prompt.txt

```text
This is an RGBA image with transparency. Shift her weight onto one leg with the opposite knee relaxed, moving the hips slightly toward screen-right. Turn the torso gently toward screen-left while keeping the face directed toward the viewer. Lean forward a little as if inviting a response. Extend one forearm toward screen-left at lower-chest height with the palm open upward and a clear gap between elbow and waist. Bend the other arm with its hand resting lightly at her waist. Give the shoulders a gentle opposing tilt to the hips. Friendly engaged smile, mouth slightly open, eyes on the viewer. Full body, entire character visible with margin around head, hands and feet. Visual novel character illustration, anime style, flat anime cel shading, clean crisp lineart, soft even studio lighting. No scenery, no floor shadow, no text, no border. <image1> shows the front view of the character. <image2> shows the side view of the same character, wearing the same outfit. The image has alpha channel and the background is transparent.
```

## expected-prompt.txt

```text
This is an RGBA image with transparency. Shift her weight onto one leg with the opposite knee relaxed, moving the hips slightly toward screen-right. Turn the torso gently toward screen-left while keeping the face directed toward the viewer. Lean forward a little as if inviting a response. Extend one forearm toward screen-left at lower-chest height with the palm open upward and a clear gap between elbow and waist. Bend the other arm with its hand resting lightly at her waist. Give the shoulders a gentle opposing tilt to the hips. Friendly engaged smile, mouth slightly open, eyes on the viewer. Full body, entire character visible with margin around head, hands and feet. Visual novel character illustration, anime style, flat anime cel shading, clean crisp lineart, soft even studio lighting. No scenery, no floor shadow, no text, no border. <image1> shows the front view of the character. <image2> shows the side view of the same character, wearing the same outfit. The image has alpha channel and the background is transparent.
```

## future-prompt-not-generated.txt

```text
This is an RGBA image with transparency. Pose the character shown in the reference images as follows. Shift her weight onto one leg with the opposite knee relaxed, moving the hips slightly toward screen-right. Turn the torso gently toward screen-left while keeping the face directed toward the viewer. Lean forward a little as if inviting a response. Extend one forearm toward screen-left at lower-chest height with the palm open upward and a clear gap between elbow and waist. Bend the other arm with its hand resting lightly at her waist. Give the shoulders a gentle opposing tilt to the hips. Friendly engaged smile, mouth slightly open, eyes on the viewer. Full body, entire character visible with margin around head, hands and feet. Visual novel character illustration, anime style, flat anime cel shading, clean crisp lineart, soft even studio lighting. No scenery, no floor shadow, no text, no border. <image1> shows the front view of the character. <image2> shows the side view of the same character, wearing the same outfit. The image has alpha channel and the background is transparent.
```

## submitted-request.json

```json
{
  "poses": [
    {
      "name": "speaking",
      "seed": 12345,
      "prompt": "Shift her weight onto one leg with the opposite knee relaxed, moving the hips slightly toward screen-right. Turn the torso gently toward screen-left while keeping the face directed toward the viewer. Lean forward a little as if inviting a response. Extend one forearm toward screen-left at lower-chest height with the palm open upward and a clear gap between elbow and waist. Bend the other arm with its hand resting lightly at her waist. Give the shoulders a gentle opposing tilt to the hips. Friendly engaged smile, mouth slightly open, eyes on the viewer."
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