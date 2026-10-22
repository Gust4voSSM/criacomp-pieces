# Prompts — Híbrido humano-kobold — workflow refatorado

Textos recuperados dos metadados de execução dos PNGs. As ligações entre nós são resolvidas para mostrar o texto enviado ao encoder; campos antigos desconectados não são tratados como prompts executados.

## Descrição compartilhada

```text
A young male human-kobold hybrid of average height, with dark skin and a blend of human and reptilian features. He wears traditional Japanese medieval fantasy clothing, including layered robes, a short kimono, a tied sash, and loose-fitting hakama pants. His outfit features intricate fabric details, traditional Japanese patterns, and subtle fantasy-inspired accessories. A balanced mix of humanoid and kobold characteristics
```

## Frente

Especialização:

```text
standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, full-body visual novel character reference, highly detailed
```

Prompt completo (descrição + separador + especialização):

```text
A young male human-kobold hybrid of average height, with dark skin and a blend of human and reptilian features. He wears traditional Japanese medieval fantasy clothing, including layered robes, a short kimono, a tied sash, and loose-fitting hakama pants. His outfit features intricate fabric details, traditional Japanese patterns, and subtle fantasy-inspired accessories. A balanced mix of humanoid and kobold characteristics, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, full-body visual novel character reference, highly detailed
```

## Lateral

Especialização:

```text
standing straight, left side profile view, neutral calm expression, full-body visual novel character reference, consistent character design
```

Prompt completo (descrição + separador + especialização):

```text
A young male human-kobold hybrid of average height, with dark skin and a blend of human and reptilian features. He wears traditional Japanese medieval fantasy clothing, including layered robes, a short kimono, a tied sash, and loose-fitting hakama pants. His outfit features intricate fabric details, traditional Japanese patterns, and subtle fantasy-inspired accessories. A balanced mix of humanoid and kobold characteristics, standing straight, left side profile view, neutral calm expression, full-body visual novel character reference, consistent character design
```

## Feliz / aceno

Especialização:

```text
cheerful happy smiling expression, waving one hand, friendly standing pose, visual novel sprite
```

Prompt completo (descrição + separador + especialização):

```text
A young male human-kobold hybrid of average height, with dark skin and a blend of human and reptilian features. He wears traditional Japanese medieval fantasy clothing, including layered robes, a short kimono, a tied sash, and loose-fitting hakama pants. His outfit features intricate fabric details, traditional Japanese patterns, and subtle fantasy-inspired accessories. A balanced mix of humanoid and kobold characteristics, cheerful happy smiling expression, waving one hand, friendly standing pose, visual novel sprite
```

## Surpresa

Especialização:

```text
surprised shocked expression, eyes wide open, both hands raised near chest, standing pose, visual novel sprite
```

Prompt completo (descrição + separador + especialização):

```text
A young male human-kobold hybrid of average height, with dark skin and a blend of human and reptilian features. He wears traditional Japanese medieval fantasy clothing, including layered robes, a short kimono, a tied sash, and loose-fitting hakama pants. His outfit features intricate fabric details, traditional Japanese patterns, and subtle fantasy-inspired accessories. A balanced mix of humanoid and kobold characteristics, surprised shocked expression, eyes wide open, both hands raised near chest, standing pose, visual novel sprite
```

## Tristeza

Especialização:

```text
sad teary crying expression, looking down slightly, hands clasped together in front, standing pose, visual novel sprite
```

Prompt completo (descrição + separador + especialização):

```text
A young male human-kobold hybrid of average height, with dark skin and a blend of human and reptilian features. He wears traditional Japanese medieval fantasy clothing, including layered robes, a short kimono, a tied sash, and loose-fitting hakama pants. His outfit features intricate fabric details, traditional Japanese patterns, and subtle fantasy-inspired accessories. A balanced mix of humanoid and kobold characteristics, sad teary crying expression, looking down slightly, hands clasped together in front, standing pose, visual novel sprite
```

## Parâmetros e referências

FLUX.2 Dev (`flux2_dev_fp8mixed.safetensors`), encoder Mistral, VAE FLUX.2, imagens de 768 × 1152. Os parâmetros completos, seeds e referências estão em [workflow.json](workflow.json) e nos arquivos `*.prompt.json`. A lateral usa a frente; as três poses usam as duas vistas. A remoção de fundo usa BiRefNet.
