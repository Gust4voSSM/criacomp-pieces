# Primeiro teste Qwen na Modal

Execução: 21/10/2026, ComfyUI na Modal, L40S. Frente (seed 1), lateral (seed 2) e pose feliz (seed 1). A pose preservou a postura neutra da frente.

[Baixar esta geração em ZIP](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-qwen-image-21/evidencias/primeira-run/primeira-run.zip) · [Prompts](prompts.md) · [Workflow para o editor](workflow.json) · [Grafo executado](workflow-original.api.json) · [Proveniência](proveniencia.json)

Os PNGs originais foram copiados sem alteração. Os metadados disponíveis foram extraídos em JSONs ao lado de cada imagem. `summary.json`, `history.json` e `comfy.log` preservam métricas e registro da execução. As duas execuções usam Qwen-Image-2.1 base BF16, 768 × 1152, 40 passos, CFG 1 e Euler/simple.

## Reproduzir

Copie `custom_nodes/vn_qwen` para o ComfyUI e reinicie. Importe `workflow.json` no editor. `workflow.api.json` é a versão de API; `workflow-original.api.json` preserva o grafo executado.

Pesos: `qwen_image_2.1_bf16.safetensors`, `qwen3vl_8b_bf16.safetensors` e `qwen_image_2.1_vae_bf16.safetensors`, nos diretórios de modelos correspondentes do ComfyUI. A execução exige uma versão compatível com TextEncodeQwenImage21; o commit usado está na proveniência.

## Imagens geradas

### charsheet_front_rgba_00001_.png

![charsheet_front_rgba_00001_.png](charsheet_front_rgba_00001_.png)

### charsheet_side_rgba_00001_.png

![charsheet_side_rgba_00001_.png](charsheet_side_rgba_00001_.png)

### sprite_happy_rgba_00001_.png

![sprite_happy_rgba_00001_.png](sprite_happy_rgba_00001_.png)

O ZIP inclui esta pasta, prompts, imagens, referências quando usadas, workflows, custom nodes, logs, proveniência e SHA256SUMS.txt. O próprio ZIP fica fora da compactação.
