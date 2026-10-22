# Sprites de visual novel com Qwen-Image-2.1 na Modal

Continuação do [experimento com o agente do ComfyUI Cloud](../vn-sprites-agentico/). Depois dos problemas na remoção de fundo com BiRefNet, o workflow foi adaptado para gerar referências e sprites diretamente em RGBA com Qwen-Image-2.1.

## Gerações e outputs

| Pasta | Conteúdo | Prompts | ZIP |
| --- | --- | --- | --- |
| [Primeira geração](evidencias/primeira-run/) | Duas referências e uma pose; a pose feliz repetiu a postura neutra | [prompts.md](evidencias/primeira-run/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-qwen-image-21/evidencias/primeira-run/primeira-run.zip) |
| [Seed 12345](evidencias/seed-12345-run/) | Uma nova pose feliz, sorrindo e acenando; duas referências reutilizadas incluídas | [prompts.md](evidencias/seed-12345-run/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-qwen-image-21/evidencias/seed-12345-run/seed-12345-run.zip) |

Cada pasta reúne PNGs originais, metadados extraídos, prompts completos, workflow para o editor, grafo de API executado, custom nodes, histórico, logs, resumo e proveniência com SHA-256. Os workflows do editor foram reconstruídos; no segundo teste os caminhos das referências foram adaptados para reprodução local, mantendo o grafo original em arquivo separado.

São quatro imagens geradas ao todo. O download da API é uma cópia da primeira execução e não é contado como outra geração. As referências incluídas na segunda pasta são cópias exatas das duas primeiras imagens. Surpresa e tristeza não foram executadas nesses testes.

O primeiro teste levou 107,44 s; o segundo, com apenas uma imagem nova, 79,34 s. Ambos incluem a inicialização do ComfyUI e excluem o download inicial dos modelos e a montagem do ambiente. A troca da seed da pose de 1 para 12345 acompanhou o sorriso e o aceno pedidos. A investigação local e o [relato no Diffusers](https://github.com/huggingface/diffusers/issues/14824) sustentam a hipótese de noise replay; a recarga de referências PNG de 8 bits também difere do primeiro teste. A API de produção não foi alterada por esse teste isolado.

## Downloads por geração

- [Primeira geração — ZIP](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-qwen-image-21/evidencias/primeira-run/primeira-run.zip)
- [Seed 12345 — ZIP](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-qwen-image-21/evidencias/seed-12345-run/seed-12345-run.zip)

Cada ZIP tem sua pasta de geração como diretório raiz e inclui SHA256SUMS.txt. Para regenerar os arquivos, execute `python scripts/package_experiments.py` na raiz do repositório.

## Ferramentas e referências

- [Qwen-Image-2.1 — documentação e transparência nativa](https://github.com/QwenLM/Qwen-Image-2.1)
- [Pesos para ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image-2.1)
- [ComfyUI](https://github.com/Comfy-Org/ComfyUI)
- [Modal](https://modal.com/)
