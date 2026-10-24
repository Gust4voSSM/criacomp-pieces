# Máscara primeiro, RGB depois

image_gen gerou `mask.png` a partir das referências frente, lado e pose acenando da segunda geração ComfyUI Cloud (refatorado-run de Gust4voSSM/criacomp-pieces). Depois recebeu essas três referências mais a máscara e gerou `pose-rgb.png`, instruído a seguir exatamente a silhueta. Prompts em `prompts.txt`.

Ambos têm 1024 × 1536 pixels. Pillow aplicou a luminância da máscara como A sem redimensionar ou corrigir a geometria: `pose-rgba.png`. Nenhuma limpeza ou alinhamento posterior. O RGB original foi preservado.

A máscara tem palma e punho contínuos, sem os cortes internos da tentativa RGB-primeiro. Entretanto, o RGB não seguiu exatamente o contorno: na composição sobre branco aparecem franjas pretas e cortes de borda, inclusive nos dedos. `hand-check.png` mostra a região ampliada. Não aprovar este RGBA como asset final.

Comparação com OpenCV: `../flux2-aceno-alpha/compare_rgb_alpha.py --mask-first`. Escala comum de análise 768 × 1152; arquivo final permanece 1024 × 1536. Com Canny 60/160, contorno A a até 1 px de borda RGB: RGB-primeiro 97,36%; máscara-primeiro 71,23%; Qwen Spaces 98,93%. Distância média: 0,382 / 1,060 / 0,436 px. O resultado máscara-primeiro também foi inferior nos outros dois pares de limiares testados.

Esses números medem alinhamento de contorno, não qualidade absoluta. A tentativa RGB-primeiro continua reprovada pelos cortes internos na mão, apesar de sua pontuação alta. Uma geração por método não permite concluir que a ordem seja a causa da diferença. Não há condicionamento rígido por máscara exposto na ferramenta: a máscara foi fornecida como imagem de referência com instruções textuais.

Resultados: `rgb-vs-alpha.png`, `rgb-vs-alpha-details.png`, `rgb-vs-alpha-metrics.json`. Limites do método em `../flux2-aceno-alpha/RGB-vs-A.md`.
