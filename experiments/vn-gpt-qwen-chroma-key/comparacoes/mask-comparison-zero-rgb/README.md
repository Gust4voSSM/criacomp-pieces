# Comparação RGB × alpha após zerar RGB em A = 0

Mesmo método OpenCV anterior: Canny por canal RGB (60/160), contorno interno em A >= 128, distância euclidiana. Análise em 768 × 1152, canais redimensionados separadamente com Lanczos. Os outros dois limiares anteriores também foram executados. Não houve nova inferência.

| Resultado | Até 1 px: original | Até 1 px: RGB zero em A=0 | Distância média após limpeza |
| --- | ---: | ---: | ---: |
| Atual: falando | 99.60% | 99.63% | 0.315 px |
| Atual: ouvindo | 99.10% | 99.32% | 0.307 px |
| Atual: refletindo | 99.80% | 99.73% | 0.277 px |
| Anterior: falando | 99.37% | 99.64% | 0.341 px |
| Anterior: ouvindo | 99.22% | 99.37% | 0.305 px |
| Anterior: refletindo | 99.64% | 99.51% | 0.287 px |
| FLUX + BiRefNet | 99.16% | 99.16% | 0.323 px |
| FLUX + mascara GPT | 90.56% | 91.41% | 0.573 px |
| GPT RGB primeiro | 97.36% | 97.48% | 0.381 px |
| GPT mascara primeiro | 71.23% | 72.35% | 1.027 px |
| Qwen Spaces | 98.93% | 95.76% | 0.573 px |
| Qwen Modal seed 12345 | 99.67% | 98.42% | 0.555 px |

## O que a limpeza altera

Foram criadas cópias de todas as 12 variantes com o mesmo critério, para comparar de forma consistente. Apenas RGB de pixels com A exatamente zero foi zerado. Nenhum alpha foi modificado; RGB em A > 0 também não foi modificado. Arquivos de origem preservados. Os três sprites atuais estão em current-cleaned/.

As composições nativas antes/depois são idênticas pixel a pixel sobre branco, azul escuro e verde: o RGB invisível não participa da composição correta. Um gerador de miniaturas ou redimensionamento que trate RGB e A separadamente pode vazar essas cores; a limpeza só resolve a parcela A=0, não o RGB colorido em A=1 ou A=2.

A detecção de bordas RGB muda. Exemplo: Qwen Spaces cai de 98,93% para 95,76%; os atuais ficam entre 99,32% e 99,73%. Isso não significa que o alpha melhorou ou piorou, pois ele é exatamente o mesmo. Zerá-lo cria/remove transições no próprio RGB junto da fronteira determinada por A; portanto, há dependência entre RGB e máscara e a métrica não é um validador independente de qualidade.

A distância média e a taxa dentro de 1 px podem apontar direções diferentes porque medem aspectos diferentes da distribuição. O corpo/pose/artwork também difere entre experimentos, então esta tabela é descritiva, não um ranking controlado de modelos. O defeito interno de mão do GPT RGB-primeiro continua grave, apesar da boa pontuação.

## Inspeção visual

page-01.png: atuais; page-02.png: lote anterior; page-03.png: FLUX/BiRefNet, máscara GPT/FLUX, GPT RGB-primeiro; page-04.png: GPT máscara-primeiro, Qwen Spaces e Qwen Modal antigo. Branco, escuro, xadrez, alpha e sobreposição RGB × A. Magenta = alpha, ciano = bordas RGB próximas. As prévias de composição usam resize RGBA premultiplicado do Pillow para não introduzir vazamento de RGB oculto; as métricas mantêm a interpolação independente do método anterior.

Nas mãos atuais ampliadas, não observei os cortes internos que reprovaram a máscara GPT anterior. Isso não certifica todos os pixels. O resultado ouvindo continua uma quase cópia da frente; isso é uma questão de edição/pose e não é explicado nem corrigido pela limpeza de RGB invisível.

Código reproduzível: ../compare_all_masks.py --zero-transparent-rgb. Métricas brutas: ../mask-comparison-all/metrics.json. Métricas limpas: metrics.json e metrics.csv. Checks de invariância: cleanup-verification.json.
