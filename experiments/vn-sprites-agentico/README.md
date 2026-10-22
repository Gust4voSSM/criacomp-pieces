# Sprites de visual novel com o agente do ComfyUI Cloud

Experimento sobre transformar um pedido em linguagem natural em um workflow para produzir referências de personagem, poses e sprites com transparência.

[Relato do experimento (rascunho)](rascunho.md) · [Comparação antes/depois](comparacao.md) · [Diferenças entre os prompts da personagem](prompts-completos.md)

## Gerações e outputs

| Pasta | Conteúdo | Prompts |
| --- | --- | --- |
| [Primeira geração](evidencias/primeira-run/) | Personagem de cabelo prateado, workflow inicial; duas referências e três sprites | [prompts.md](evidencias/primeira-run/prompts.md) |
| [Segunda geração](evidencias/refatorado-run/) | Mesma personagem, workflow refatorado; duas referências e três sprites | [prompts.md](evidencias/refatorado-run/prompts.md) |
| [Kobold](evidencias/kobold-run/) | Híbrido humano-kobold com a descrição compartilhada trocada; duas referências e três sprites | [prompts.md](evidencias/kobold-run/prompts.md) |

Cada pasta inclui os cinco PNGs originais, `workflow.json` para importar no ComfyUI, os metadados de cada imagem e a proveniência com SHA-256. Os textos completos enviados ao modelo estão no `prompts.md` de cada geração.

As [visualizações do alpha](evidencias/alpha-original/) mostram o recorte das duas gerações da personagem de cabelo prateado; são evidências derivadas, separadas dos PNGs originais.

O relato preserva o rascunho existente e trata das duas gerações da personagem. O Kobold está incluído aqui como execução adicional do workflow refatorado, com seus próprios outputs e prompts.

## Download direto

[Baixar todo o experimento em ZIP](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-sprites-agentico/vn-sprites-agentico.zip)

O GitHub Raw entrega arquivos individuais; uma URL de pasta não produz um ZIP. Por isso, `vn-sprites-agentico.zip` está nesta pasta para acesso direto pelo Raw. O arquivo contém os documentos, os outputs, os prompts e os workflows deste experimento; não inclui uma cópia de si mesmo.

Para baixar somente um workflow pelo Raw:

- [Workflow inicial](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-sprites-agentico/evidencias/primeira-run/workflow.json)
- [Workflow refatorado — personagem](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-sprites-agentico/evidencias/refatorado-run/workflow.json)
- [Workflow refatorado — Kobold](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-sprites-agentico/evidencias/kobold-run/workflow.json)

`SHA256SUMS.txt` permite conferir a integridade dos arquivos individuais. Para atualizar o ZIP após uma edição, execute `python scripts/package_experiments.py` na raiz do repositório.

## Ferramentas e referências

- [Comfy Agent](https://support.comfy.org/articles/4013072355-comfy-agent)
- [Comfy Cloud](https://cloud.comfy.org/)
- [FLUX.2 Dev](https://huggingface.co/black-forest-labs/FLUX.2-dev)
- [BiRefNet](https://github.com/ZhengPeng7/BiRefNet)
