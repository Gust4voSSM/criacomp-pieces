# criacomp-pieces

Experimentos e registros de processo de Gustavo Santiago para a disciplina Criatividade Computacional (IF866), CIn–UFPE.

Cada experimento reúne o que foi tentado, as ferramentas e os prompts utilizados, os resultados e os aprendizados. Os arquivos de geração preservam seus metadados sempre que disponíveis.

## Experimentos

| Experimento | Conteúdo | Download |
| --- | --- | --- |
| [Sprites de visual novel com o agente do ComfyUI Cloud](experiments/vn-sprites-agentico/) | Workflow inicial, refatoração e execução com Kobold; 15 imagens, prompts e workflows | [ZIP direto](https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-sprites-agentico/vn-sprites-agentico.zip) |

## Organização

```text
experiments/
  vn-sprites-agentico/
    README.md
    rascunho.md
    comparacao.md
    prompts-completos.md
    evidencias/
      primeira-run/     # imagens, prompts.md e workflows
      refatorado-run/   # imagens, prompts.md e workflows
      kobold-run/       # imagens, prompts.md e workflows
      alpha-original/  # visualizações do canal alpha
    SHA256SUMS.txt
    vn-sprites-agentico.zip
scripts/
  package_experiments.py
```

## Contexto da disciplina

O [repositório oficial da disciplina](https://github.com/filipecalegario/criacomp) reúne a contextualização, as orientações de avaliação, as notícias e as skills. Este repositório reúne meus experimentos e seus arquivos.

## Downloads

Os links de ZIP em cada experimento baixam os arquivos diretamente pelo GitHub Raw. O Raw não compacta pastas; os ZIPs são preparados e versionados no repositório. Para regenerá-los, use `python scripts/package_experiments.py` (somente biblioteca padrão do Python).
