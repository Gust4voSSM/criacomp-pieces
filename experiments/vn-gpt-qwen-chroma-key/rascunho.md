# Chroma key em sprites de visual novel: uma surpresa com GPT Image

## O que quis tentar

Na última peça, planejei gerar o character sheet com um modelo de imagem da OpenAI e usar essas referências no Qwen-Image-2.1 para criar poses transparentes. Também queria testar CFG maior que 1, já que algumas imagens do Qwen tinham problemas nos olhos e nas mãos.

Continuei com a personagem de cabelo prateado e uniforme azul. Não estava satisfeito com as edições do Qwen por conta dos artefatos nas mãos, então quis tentar gerar também as poses com o próprio GPT Image. Para obter os sprites transparentes, resolvi pedir um fundo de cor sólida e removê-lo depois por chroma key. Eu acreditava que conseguir boas máscaras por esse caminho seria mais difícil.

## O que usei

Usei o gerador de imagens integrado ao Codex para criar a frente e a lateral em arquivos separados, com a lateral condicionada pela frente. As duas referências saíram em RGB, sobre preto, em 1024 × 1536. As gerações GPT deste experimento foram feitas pela ferramenta integrada; o uso por API ficou para a etapa de automação.

Para as poses com transparência nativa, usei Qwen-Image-2.1 no ComfyUI executado na Modal, com as duas referências GPT. Mantive 40 passos, sampler Euler e scheduler simple, inicialmente com CFG 1. No teste de CFG 2, comparei uma geração sem negative prompt com outra usando uma lista de negativos, mantendo o mesmo prompt positivo, referências e seed.

Para o chroma key, gerei três poses com GPT Image usando as mesmas referências e descrições de pose do lote inicial do Qwen, substituindo o pedido de transparência por fundo verde. O recorte foi feito em Python com OpenCV e NumPy, com alpha suave e correção da cor do fundo nas bordas. Também usei um script de comparação entre o contorno do alpha e as bordas do RGB, além de composições sobre fundos claros e escuros para inspecionar os resultados.

## O que aconteceu

O fluxo GPT Image → Qwen funcionou bem para gerar os sprites. Pedi poses de falando, ouvindo e refletindo. A pose ouvindo ficou muito próxima da referência frontal, e inicialmente suspeitei de noise replay. Ao conferir o fluxo, vimos que o prompt pedia praticamente a postura que já estava na referência: braços baixos, boca fechada e olhar para a frente.

Essa semelhança me incomodou porque, quando a silhueta permanece quase igual, as pequenas diferenças do redesenho ficam mais perceptíveis. Pedi poses mais distintas. Gostei muito da nova pose refletindo. A de falando ficou estranha, com uma perna levantada e problemas nas mãos. O prompt descrevia vários ajustes de quadril, joelho, ombros e braços, e o resultado parecia aleatório para uma conversa. Simplificar o gesto e pedir os dois pés no chão melhorou a postura.

Com CFG 2, a mão apoiada no quadril ficou melhor tanto na versão com negativos quanto na versão sem eles. Nesse teste, o benefício adicional da lista de negativos ficou pouco claro.

Também testei pedir ao GPT uma máscara separada da imagem. Uma das versões abriu cortes dentro da mão e do punho, mesmo pontuando acima de 97% na comparação de bordas. Inverter a ordem, gerando primeiro a máscara e depois o desenho, deixou desalinhamentos e franjas pretas.

Ainda insatisfeito com os artefatos nas mãos nas edições do Qwen, passei a testar as poses com o próprio GPT Image sobre fundo verde. A ideia era remover o fundo por chroma key, e tive uma surpresa agradável com o recorte. As máscaras ficaram comparáveis às que consegui com referências GPT e alpha nativo do Qwen. O recorte suave preservou os espaços entre dedos e as principais aberturas no cabelo; nas mechas finas ainda apareceu alguma contaminação de cor. O alinhamento do contorno a até um pixel das bordas do desenho ficou entre 98,60% e 99,50% no chroma key, e entre 99,10% e 99,80% no lote Qwen usado na comparação.

Para testar um design com cores que poderiam atrapalhar o recorte, pedi uma arara antropomórfica com penas vermelhas, verdes e azuis. O recorte verde mais simples apagou ou deixou transparentes partes das penas verdes. Ajustar o recorte pela distância até a cor do fundo preservou melhor as penas, porém a franja verde continuou muito perceptível e achei o acabamento insuficiente.

Pedi então um fundo magenta. A troca da cor ainda deixou franjas com o método anterior. Com uma estimativa de alpha específica para magenta e correção da cor dos pixels de borda, o resultado ficou mais limpo, preservando as penas verdes.

## O que aprendi

O chroma key funcionou surpreendentemente bem para esse tipo de personagem de visual novel. São desenhos com line art bem definida e uma silhueta opaca, sem materiais transparentes para recuperar. Nesse contexto, consegui máscaras comparáveis às do fluxo Image-Gen + Qwen com uma etapa de recorte procedural.

Isso me fez considerar gerar tanto as referências quanto as poses com o modelo da OpenAI. Para automatizar esse caminho, quero escolher uma cor de fundo suficientemente distante das cores da personagem e medir a cor que o modelo realmente gerou, usando amostras dos cantos e das bordas. O verde pedido no prompt pode sair com valores um pouco diferentes. Quando houver conflito de cores ou um recorte ruim, a ideia é recorrer ao Qwen para obter RGBA a partir de uma imagem sobre preto.

Também ficou mais claro para mim o quanto os prompts das poses interferem no resultado. Quero manter a identidade da personagem e dar mais variedade às silhuetas, com gestos que façam sentido numa conversa. A pose refletindo funcionou bem; a de falando melhorou quando o pedido ficou mais simples.

As comparações numéricas de bordas ajudaram a investigar os resultados, mas precisei olhar as mãos, o cabelo e as franjas sobre fundos diferentes. Tanto os cortes na mão quanto o contorno verde da arara passaram com pontuações altas.

