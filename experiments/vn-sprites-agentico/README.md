# Sprites de visual novel com o agente do ComfyUI Cloud

Experimento sobre transformar um pedido em linguagem natural em um workflow para produzir referências de personagem, poses e sprites com transparência.

[Relato do experimento (rascunho)](rascunho.md) · [Comparação antes/depois](comparacao.md) · [Diferenças entre os prompts da personagem](prompts-completos.md)

## Gerações e outputs

| Pasta | Conteúdo | Prompts | ZIP |
| --- | --- | --- | --- |
| [Primeira geração](evidencias/primeira-run/) | Personagem de cabelo prateado, workflow inicial; duas referências e três sprites | [prompts.md](evidencias/primeira-run/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-sprites-agentico/evidencias/primeira-run/primeira-run.zip) |
| [Segunda geração](evidencias/refatorado-run/) | Mesma personagem, workflow refatorado; duas referências e três sprites | [prompts.md](evidencias/refatorado-run/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-sprites-agentico/evidencias/refatorado-run/refatorado-run.zip) |
| [Kobold](evidencias/kobold-run/) | Híbrido humano-kobold com a descrição compartilhada trocada; duas referências e três sprites | [prompts.md](evidencias/kobold-run/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-sprites-agentico/evidencias/kobold-run/kobold-run.zip) |

Cada pasta inclui os cinco PNGs originais, `workflow.json` para importar no ComfyUI, os metadados de cada imagem e a proveniência com SHA-256. Os textos completos enviados ao modelo estão no `prompts.md` de cada geração.

As [visualizações do alpha](evidencias/alpha-original/) mostram o recorte das duas gerações da personagem de cabelo prateado; são evidências derivadas, separadas dos PNGs originais.

O relato preserva o rascunho existente e trata das duas gerações da personagem. O Kobold está incluído aqui como execução adicional do workflow refatorado, com seus próprios outputs e prompts.

## Downloads por geração

Cada pasta de geração tem um único `prompts.md` e um ZIP com o conteúdo dessa pasta: imagens, prompts, workflows, proveniência e hashes. O ZIP inclui a pasta da geração como diretório raiz e exclui o próprio arquivo ZIP.

- [Primeira geração — ZIP](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-sprites-agentico/evidencias/primeira-run/primeira-run.zip)
- [Segunda geração — ZIP](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-sprites-agentico/evidencias/refatorado-run/refatorado-run.zip)
- [Kobold — ZIP](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-sprites-agentico/evidencias/kobold-run/kobold-run.zip)

Os links baixam pelo GitHub Raw, que serve arquivos individuais e não compacta pastas. O `SHA256SUMS.txt` de cada geração permite conferir seus arquivos. Para regenerar os ZIPs após uma edição, execute `python scripts/package_experiments.py` na raiz do repositório.

## Ferramentas e referências

- [Comfy Agent](https://support.comfy.org/articles/4013072355-comfy-agent)
- [Comfy Cloud](https://cloud.comfy.org/)
- [FLUX.2 Dev](https://huggingface.co/black-forest-labs/FLUX.2-dev)
- [BiRefNet](https://github.com/ZhengPeng7/BiRefNet)
