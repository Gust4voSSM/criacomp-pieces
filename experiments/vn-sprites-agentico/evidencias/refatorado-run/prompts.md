# Prompts — Personagem de cabelo prateado — workflow refatorado

Textos recuperados dos metadados de execução dos PNGs. As ligações entre nós são resolvidas para mostrar o texto enviado ao encoder; campos antigos desconectados não são tratados como prompts executados.

## Descrição compartilhada

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid black background, soft even studio lighting, highly detailed
```

## Frente

Especialização:

```text
standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, full-body visual novel character reference, highly detailed
```

Prompt completo (descrição + separador + especialização):

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid black background, soft even studio lighting, highly detailed, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, full-body visual novel character reference, highly detailed
```

## Lateral

Especialização:

```text
standing straight, left side profile view, neutral calm expression, full-body visual novel character reference, consistent character design
```

Prompt completo (descrição + separador + especialização):

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid black background, soft even studio lighting, highly detailed, standing straight, left side profile view, neutral calm expression, full-body visual novel character reference, consistent character design
```

## Feliz / aceno

Especialização:

```text
cheerful happy smiling expression, waving one hand, friendly standing pose, visual novel sprite
```

Prompt completo (descrição + separador + especialização):

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid black background, soft even studio lighting, highly detailed, cheerful happy smiling expression, waving one hand, friendly standing pose, visual novel sprite
```

## Surpresa

Especialização:

```text
surprised shocked expression, eyes wide open, both hands raised near chest, standing pose, visual novel sprite
```

Prompt completo (descrição + separador + especialização):

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid black background, soft even studio lighting, highly detailed, surprised shocked expression, eyes wide open, both hands raised near chest, standing pose, visual novel sprite
```

## Tristeza

Especialização:

```text
sad teary crying expression, looking down slightly, hands clasped together in front, standing pose, visual novel sprite
```

Prompt completo (descrição + separador + especialização):

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid black background, soft even studio lighting, highly detailed, sad teary crying expression, looking down slightly, hands clasped together in front, standing pose, visual novel sprite
```

## Parâmetros e referências

FLUX.2 Dev (`flux2_dev_fp8mixed.safetensors`), encoder Mistral, VAE FLUX.2, imagens de 768 × 1152. Os parâmetros completos, seeds e referências estão em [workflow.json](workflow.json) e nos arquivos `*.prompt.json`. A lateral usa a frente; as três poses usam as duas vistas. A remoção de fundo usa BiRefNet.
