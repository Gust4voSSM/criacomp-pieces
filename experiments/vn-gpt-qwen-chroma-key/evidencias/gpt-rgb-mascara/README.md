# Pose GPT seguida de máscara GPT

Referências: charsheets frente e lado da segunda geração do experimento ComfyUI Cloud, no repositório Gust4voSSM/criacomp-pieces, pasta experiments/vn-sprites-agentico/evidencias/refatorado-run. O autor identificou essas referências nesta conversa. Os arquivos do repositório documentam FLUX.2 Dev; não se atribui a geração deles ao Klein.

https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-sprites-agentico/evidencias/refatorado-run/charsheet_front_00001_.png

https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-sprites-agentico/evidencias/refatorado-run/charsheet_side_00001_.png

1. image_gen gerou `pose-rgb.png` a partir das duas referências: pose sorrindo e acenando, fundo preto, 1024 × 1536.
2. Outra chamada image_gen gerou `pose-mask.png` usando exclusivamente a nova pose como alvo. Saída 1024 × 1536.
3. Pillow converteu a máscara para luminância L e aplicou como canal A, preservando integralmente RGB. Resultado: `pose-rgba.png`, 1024 × 1536. Sem redimensionamento na composição, alinhamento posterior ou limpeza.

Os prompts completos estão em `prompts.txt`.

## RGB versus alpha

Reprodução: executar `../flux2-aceno-alpha/compare_rgb_alpha.py --new-pose` com Python, Pillow, OpenCV e NumPy. Para comparar com os experimentos anteriores, somente a análise usa escala comum 768 × 1152. O RGBA final permanece 1024 × 1536.

| Versão | Contorno A até 1 px de borda RGB | Até 2 px | Distância média |
| --- | ---: | ---: | ---: |
| GPT máscara sobre FLUX original | 90,56% | 98,59% | 0,585 px |
| GPT pose nova + GPT máscara | 97,36% | 99,76% | 0,382 px |
| Qwen Spaces nativo | 98,93% | 99,98% | 0,436 px |

Valores Canny 60/160. A melhora da nova pose GPT sobre a máscara do FLUX aparece também nos limiares 30/80 e 100/200. Qwen tem maior proporção do contorno dentro de 1 px; GPT novo tem menor distância média. Nenhuma métrica isolada permite declarar superioridade geral.

Limites: agora a ilustração também é diferente, incluindo posição do rabo de cavalo e proporções; não é um teste isolado do redimensionamento. Uma amostra por condição não separa efeito de tamanho, contraste, complexidade do contorno e variação generativa. Canny mede proximidade a bordas RGB, não precisão de segmentação anotada. A máscara pode manter detalhes errados ou gerar falhas mesmo com boa pontuação. Veja os limites completos do método em `../flux2-aceno-alpha/RGB-vs-A.md`.

`rgb-vs-alpha.png` compara as três versões (RGB sem alpha, A, fundo branco, sobreposição). `rgb-vs-alpha-metrics.json` contém todos os limiares. A composição e as dimensões foram verificadas por software; RGB final é idêntico ao da pose nova.
