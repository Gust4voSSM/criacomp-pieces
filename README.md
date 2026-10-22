# criacomp-pieces

Experimentos e registros de processo de Gustavo Santiago para a disciplina Criatividade Computacional (IF866), CIn–UFPE.

Cada experimento reúne o que foi tentado, as ferramentas e os prompts utilizados, os resultados e os aprendizados. Os arquivos de geração preservam seus metadados sempre que disponíveis.

## Experimentos

| Experimento | Conteúdo | Download |
| --- | --- | --- |
| [Sprites de visual novel com o agente do ComfyUI Cloud](experiments/vn-sprites-agentico/) | Workflow inicial, refatoração e execução com Kobold; 15 imagens, prompts e workflows | [ZIPs por geração](experiments/vn-sprites-agentico/#downloads-por-geração) |
| [Sprites de visual novel com Qwen-Image-2.1 na Modal](experiments/vn-qwen-image-21/) | RGBA nativo, duas execuções, quatro imagens geradas e teste de seed; referências, prompts e workflows | [ZIPs por geração](experiments/vn-qwen-image-21/#downloads-por-geração) |

## Organização

```text
experiments/
  vn-sprites-agentico/
    README.md
    rascunho.md
    comparacao.md
    prompts-completos.md
    evidencias/
      primeira-run/     # imagens, prompts.md, workflows e ZIP
      refatorado-run/   # imagens, prompts.md, workflows e ZIP
      kobold-run/       # imagens, prompts.md, workflows e ZIP
      alpha-original/  # visualizações do canal alpha
  vn-qwen-image-21/
    README.md
    evidencias/
      primeira-run/     # duas referências e uma pose, prompts, workflows e ZIP
      seed-12345-run/   # nova pose, referências reutilizadas, prompts, workflows e ZIP
scripts/
  package_experiments.py
```

## Contexto da disciplina

O [repositório oficial da disciplina](https://github.com/filipecalegario/criacomp) reúne a contextualização, as orientações de avaliação, as notícias e as skills. Este repositório reúne meus experimentos e seus arquivos.

## Downloads

Cada geração tem um arquivo `prompts.md` e um ZIP que compacta sua própria pasta. Os links de ZIP baixam os arquivos diretamente pelo GitHub Raw. O Raw não compacta pastas; os ZIPs são preparados e versionados no repositório. Para regenerá-los, use `python scripts/package_experiments.py` (somente biblioteca padrão do Python).
