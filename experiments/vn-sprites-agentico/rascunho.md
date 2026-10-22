Sprites de visual novel com o agente do ComfyUI Cloud: funcional na primeira tentativa

O que quis tentar

Quis testar se o agente do próprio ComfyUI Cloud conseguiria transformar um pedido em linguagem natural em um workflow funcional para gerar sprites de visual novel. O pedido foi:

“Create me a workflow that turns a character prompt into visual novel sprites. Prompt > Character Sheet: Two images, front and side with simple background > Generate N poses/ expressions (3 for example) following the character sheet > Remove Background for the final sprites”.

A ideia era partir de uma descrição de personagem, criar duas referências e gerar poses e expressões consistentes com elas, terminando com sprites de fundo transparente. Queria ver até onde o agente chegava com esse pedido inicial.

O que usou

Usei o agente integrado ao ComfyUI Cloud e a primeira das cinco runs gratuitas que eu tinha disponíveis. O modelo de linguagem por trás do agente não foi identificado neste registro.

O workflow recuperado das imagens da primeira execução usa FLUX.2 Dev (flux2_dev_fp8mixed.safetensors), encoder Mistral, VAE FLUX.2 e BiRefNet para remover o fundo. A geração foi configurada em 768 × 1152, com Euler, 20 passos e guidance 4.

A personagem do teste tem cabelo prateado preso de lado, olhos violetas e uniforme colegial azul, em estilo anime. As saídas foram exportadas em um ZIP com as duas referências e três sprites. Os PNGs preservam o workflow e o prompt executado nos metadados.

O que aconteceu

O agente montou a cadeia pedida e a primeira execução produziu cinco imagens: referência frontal, referência lateral e três poses — feliz acenando, surpresa com as mãos próximas ao peito e triste com as mãos unidas à frente. A lateral usa a referência frontal; as poses usam as duas referências.

A geração ficou consistente e muito boa na minha avaliação. A personagem manteve cabelo, olhos, uniforme e estilo entre as imagens, mudando pose e expressão. O acesso ao FLUX.2 Dev pelo ComfyUI Cloud ajudou a obter esse resultado.

A remoção do fundo ainda precisava de acabamento. O workflow gerou canais alpha para os três sprites e capturou a silhueta, mas observei webbing, serrilhados nas bordas, manchas de transparência no anelar e no mindinho e um efeito forte de recorte de papel (paper cutout), que atribuí ao comportamento excessivamente conservador do modelo.

O grafo ficou bagunçado e difícil de ler, com muitos fios cruzados (“noodles”). Os cinco prompts repetiam a descrição da personagem e o estilo. Pedi a refatoração em duas mensagens: reunir esse texto em uma fonte compartilhada, concatená-lo com as instruções de cada vista ou pose e colocar o ramo de geração de pose em um subgrafo reutilizável. O canvas passou de 60 nós e 93 conexões para 33 nós principais, incluindo três instâncias do subgrafo de pose, cuja definição contém 12 nós.

Também acrescentei “full-body” aos textos específicos para evitar cortes no sprite. Nas especializações frontal e lateral, o trecho mudou assim:

Antes: “visual novel character reference”
Depois: “full-body visual novel character reference”

Eu não tinha notado que o prompt original já continha “full body”, separado por vírgulas, depois de “anime style”. A nova redação repete a instrução junto de “character reference”. Com esse prompt, o problema de enquadramento foi resolvido na execução posterior: as referências e as três poses mostram o corpo inteiro, incluindo os sapatos. Na primeira execução, as pernas ficavam cortadas.

Minha hipótese é que essa repetição tenha reforçado o enquadramento desejado. Também pensei no hífen, mas não tenho evidência de um efeito específico dele. O texto compartilhado e o fundo também mudaram entre as execuções.

Preservei os cinco pares de imagens dos exports de 20/10 e 21/10 e os workflows embutidos nos PNGs. O experimento com Qwen já resolveu o problema do recorte e será publicado junto deste, em outra peça. Depois acrescentarei os links entre elas.

Prompts da primeira geração:

Textos gerados pelo agente e preservados nos metadados da primeira execução.

Frente

a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid light grey background, soft even studio lighting, highly detailed

Lateral

a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight, left side profile view, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid light grey background, soft even studio lighting, consistent character design

Feliz

a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, cheerful happy smiling expression, waving one hand, friendly standing pose, visual novel sprite, flat anime cel shading, clean crisp lineart, plain solid light grey background, soft even studio lighting

Surpresa

a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, surprised shocked expression, eyes wide open, both hands raised near chest, standing pose, visual novel sprite, flat anime cel shading, clean crisp lineart, plain solid light grey background, soft even studio lighting

Tristeza

a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, sad teary crying expression, looking down slightly, hands clasped together in front, standing pose, visual novel sprite, flat anime cel shading, clean crisp lineart, plain solid light grey background, soft even studio lighting

Textos usados na segunda geração:

Após a refatoração, cada prompt é formado pelo texto compartilhado abaixo, seguido de vírgula e da especialização correspondente. As edições manuais relatadas pelo autor aparecem nesses textos.

Texto compartilhado

a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid black background, soft even studio lighting, highly detailed

Especialização — Frente

standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, full-body visual novel character reference, highly detailed

Especialização — Lateral

standing straight, left side profile view, neutral calm expression, full-body visual novel character reference, consistent character design

Especialização — Feliz

cheerful happy smiling expression, waving one hand, friendly standing pose, visual novel sprite

Especialização — Surpresa

surprised shocked expression, eyes wide open, both hands raised near chest, standing pose, visual novel sprite

Especialização — Tristeza

sad teary crying expression, looking down slightly, hands clasped together in front, standing pose, visual novel sprite

Alterações visíveis entre os textos:
A descrição e o estilo passam a vir de um nó compartilhado.
O fundo muda de “plain solid light grey background” para “plain solid black background”.
Frente e lateral recebem “full-body visual novel character reference” nos textos específicos; antes tinham “visual novel character reference”.
O texto compartilhado da segunda geração contém também a pose frontal e “highly detailed”. Essas instruções passam a integrar os cinco prompts concatenados.
As instruções de felicidade, surpresa e tristeza continuam nos três textos específicos.

A refatoração foi solicitada ao agente em duas mensagens. O autor relatou a adição manual de “full-body” e as demais edições de texto para a segunda geração; os exports preservam os estados finais dessas edições.

O que aprendeu

O agente entregou uma primeira versão funcional a partir de um pedido curto. Depois, usei duas mensagens para melhorar a organização do grafo e fiz o ajuste manual de “full-body” nos textos específicos. A centralização dos prompts facilitou alterar a descrição da personagem sem precisar editar vários nós.

A repetição de “full-body” acompanhou uma melhora clara no enquadramento, embora eu já tivesse essa instrução em outra parte do prompt e não a tivesse percebido.

A qualidade do alpha motivou a continuação com Qwen, que já resolveu o problema do recorte. Vou registrar esse resultado em outra peça e publicar as duas juntas.

