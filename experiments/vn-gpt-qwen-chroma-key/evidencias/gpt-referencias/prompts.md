# Referências GPT: frente e lateral

Textos e requests preservados do experimento. Os grafos e metadados dos PNGs acompanham as saídas quando disponíveis. Referências GPT fornecidas separadamente como frente e lateral.

## front-prompt.txt

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid black background, soft even studio lighting, highly detailed, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, full-body visual novel character reference, highly detailed
```

## side-prompt.txt

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid black background, soft even studio lighting, highly detailed, standing straight, left side profile view, neutral calm expression, full-body visual novel character reference, consistent character design
```

## side-separate-prompt.txt

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight, left side profile view, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid black background, soft even studio lighting, highly detailed, consistent character design. The attached image is the front identity reference ONLY. Generate ONE SINGLE character in ONE SINGLE strict side profile view, facing toward the left edge of the image. Preserve exactly her character design, navy uniform, white neck scarf and gold emblems, ribbon, pleated skirt, dark thigh-high stockings and black loafers from the reference. The full body from top of hair to soles must be visible, centered on a 1024x1536 portrait canvas. This output is a separate side-view reference image. Do not show a front view, multiple characters, multiple views, panels, comparison, collage, contact sheet or turnaround sheet. One character, one side view only.

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

## vn-prompt-review.json

```json
{
  "status": "local_preflight_passed_not_submitted",
  "reference_manifest": {
    "reference_id": "61d2bfbcb43206a635023a5660305255a124e0db635ab23f22cae012d4f3a24e",
    "description": "a young woman with long silver hair in a side ponytail tied with a navy ribbon, violet eyes, wearing a navy-blue sailor school uniform with a white neck scarf and gold emblems, pleated skirt, dark thigh-high stockings and black loafers",
    "images": [
      {
        "size": [
          1024,
          1536
        ],
        "mode": "RGB",
        "sha256": "16489603aa5c7cdfd557f38af42250840a28347de4af95f4ed998d8f94fbfbc4"
      },
      {
        "size": [
          1024,
          1536
        ],
        "mode": "RGB",
        "sha256": "26350ff92423d32be23584a84b9ea324acb7a48ff6a78b7807ac0d735f2f3eab"
      }
    ],
    "order": [
      "image_1.png",
      "image_2.png"
    ]
  },
  "expected_images": 3,
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
  "concatenated_prompts": [
    {
      "name": "speaking",
      "prompt": "This is an RGBA image with transparency. a young woman with long silver hair in a side ponytail tied with a navy ribbon, violet eyes, wearing a navy-blue sailor school uniform with a white neck scarf and gold emblems, pleated skirt, dark thigh-high stockings and black loafers. gentle friendly smiling expression, mouth slightly open, one hand open near waist in a conversational gesture, other arm relaxed, front view, standing pose. Full body, entire character visible with margin around head, hands and feet. Visual novel character illustration, anime style, flat anime cel shading, clean crisp lineart, soft even studio lighting. No scenery, no floor shadow, no text, no border. The image has alpha channel and the background is transparent."
    },
    {
      "name": "listening",
      "prompt": "This is an RGBA image with transparency. a young woman with long silver hair in a side ponytail tied with a navy ribbon, violet eyes, wearing a navy-blue sailor school uniform with a white neck scarf and gold emblems, pleated skirt, dark thigh-high stockings and black loafers. calm attentive expression, mouth closed, arms relaxed at sides, looking at the viewer, front view, standing pose. Full body, entire character visible with margin around head, hands and feet. Visual novel character illustration, anime style, flat anime cel shading, clean crisp lineart, soft even studio lighting. No scenery, no floor shadow, no text, no border. The image has alpha channel and the background is transparent."
    },
    {
      "name": "thinking",
      "prompt": "This is an RGBA image with transparency. a young woman with long silver hair in a side ponytail tied with a navy ribbon, violet eyes, wearing a navy-blue sailor school uniform with a white neck scarf and gold emblems, pleated skirt, dark thigh-high stockings and black loafers. thoughtful pensive expression, mouth closed, one hand resting under chin, gaze slightly averted, front view, standing pose. Full body, entire character visible with margin around head, hands and feet. Visual novel character illustration, anime style, flat anime cel shading, clean crisp lineart, soft even studio lighting. No scenery, no floor shadow, no text, no border. The image has alpha channel and the background is transparent."
    }
  ]
}
```