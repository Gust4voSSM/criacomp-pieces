# Sprites de visual novel: GPT Image, Qwen e chroma key

Continuação do [experimento Qwen](../vn-qwen-image-21/). Referências GPT, testes de poses e CFG no Qwen, tentativas de gerar máscaras separadas e chroma key em personagens com line art.

[Peça na galeria](https://criacomp-galeria.lovable.app/peca/17ba4d6e-e498-447f-9117-3f7471b42a7a) · [Texto do rascunho](rascunho.md)

## Downloads por geração

| Geração ou lote experimental | Prompts | ZIP |
| --- | --- | --- |
| [Referências GPT: frente e lateral](evidencias/gpt-referencias/) | [prompts.md](evidencias/gpt-referencias/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-gpt-qwen-chroma-key/evidencias/gpt-referencias/gpt-referencias.zip) |
| [Qwen: primeiras três poses com referências GPT](evidencias/qwen-primeiras-poses/) | [prompts.md](evidencias/qwen-primeiras-poses/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-gpt-qwen-chroma-key/evidencias/qwen-primeiras-poses/qwen-primeiras-poses.zip) |
| [Qwen: poses com prompts compartilhados](evidencias/qwen-prompts-concatenados/) | [prompts.md](evidencias/qwen-prompts-concatenados/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-gpt-qwen-chroma-key/evidencias/qwen-prompts-concatenados/qwen-prompts-concatenados.zip) |
| [Qwen: poses mais distintas](evidencias/qwen-duas-poses/) | [prompts.md](evidencias/qwen-duas-poses/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-gpt-qwen-chroma-key/evidencias/qwen-duas-poses/qwen-duas-poses.zip) |
| [Qwen: frente e lateral explícitas no prompt](evidencias/qwen-referencias-explicitas/) | [prompts.md](evidencias/qwen-referencias-explicitas/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-gpt-qwen-chroma-key/evidencias/qwen-referencias-explicitas/qwen-referencias-explicitas.zip) |
| [Qwen: gesto de fala simplificado](evidencias/qwen-falando-simples/) | [prompts.md](evidencias/qwen-falando-simples/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-gpt-qwen-chroma-key/evidencias/qwen-falando-simples/qwen-falando-simples.zip) |
| [Qwen: CFG 2 com e sem negativos](evidencias/qwen-cfg2/) | [prompts.md](evidencias/qwen-cfg2/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-gpt-qwen-chroma-key/evidencias/qwen-cfg2/qwen-cfg2.zip) |
| [GPT: RGB seguido de máscara](evidencias/gpt-rgb-mascara/) | [prompts.md](evidencias/gpt-rgb-mascara/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-gpt-qwen-chroma-key/evidencias/gpt-rgb-mascara/gpt-rgb-mascara.zip) |
| [GPT: máscara seguida de RGB](evidencias/gpt-mascara-primeiro/) | [prompts.md](evidencias/gpt-mascara-primeiro/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-gpt-qwen-chroma-key/evidencias/gpt-mascara-primeiro/gpt-mascara-primeiro.zip) |
| [GPT: três poses sobre verde e chroma key](evidencias/gpt-chroma-verde/) | [prompts.md](evidencias/gpt-chroma-verde/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-gpt-qwen-chroma-key/evidencias/gpt-chroma-verde/gpt-chroma-verde.zip) |
| [Arara: referências, pose sobre verde e recortes](evidencias/arara-chroma-verde/) | [prompts.md](evidencias/arara-chroma-verde/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-gpt-qwen-chroma-key/evidencias/arara-chroma-verde/arara-chroma-verde.zip) |
| [Arara: pose sobre magenta e correção das bordas](evidencias/arara-chroma-magenta/) | [prompts.md](evidencias/arara-chroma-magenta/prompts.md) | [Download](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-gpt-qwen-chroma-key/evidencias/arara-chroma-magenta/arara-chroma-magenta.zip) |

Cada ZIP contém sua pasta como raiz, com prompts e SHA256SUMS.txt. PNGs copiados sem alteração; provenance.json guarda origem e hash das cópias. ZIPs antigos foram substituídos por pacotes por lote, sem ZIPs aninhados. Control e negative são as duas condições do lote CFG 2.

O alpha por chroma key é derivado do RGB; as pontuações OpenCV medem coincidência de bordas e podem deixar passar franjas ou cortes indevidos. Consulte os READMEs de cada lote para métodos e limites. As gerações GPT usaram a ferramenta integrada, sem versão exata ou seed selecionável.

Os scripts de análise preservam caminhos do workspace original; ajuste esses caminhos para reproduzir em outro checkout. Os workflows Qwen executados estão nos arquivos request-workflow.json e history.json.

## Close-ups das mãos

[Recortes e comparação CFG 1 / CFG 2](evidencias/closeups-maos/) · [Download dos close-ups (ZIP)](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-gpt-qwen-chroma-key/evidencias/closeups-maos/closeups-maos.zip)
