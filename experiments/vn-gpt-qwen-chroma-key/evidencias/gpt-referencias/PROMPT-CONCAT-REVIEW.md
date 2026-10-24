# Revisao local da concatenacao — aguardando validacao do autor

Atualizacao: o autor aprovou a execucao real. Revisao publicada e job fc-01M5NCR7T6633YH0X518ZH5VQG iniciado em 23/10/2026. A descricao abaixo preserva o estado da revisao antes da autorizacao; resultados e manifestos novos ficam em `modal-concat-run/`.

O upload proposto contem `front.png`, `side.png` e a descricao geral em `vn-reference-description.txt`. O ID do conjunto inclui os hashes dos dois arquivos, sua ordem e a descricao. Os PNGs originais nao sao alterados.

O pedido de geracao em `vn-poses-short-request.json` contem apenas nomes, seeds e textos curtos de pose. Ao enviar ao servidor, recebe tambem o reference_id retornado pelo upload.

O backend recupera a descricao associada ao par e usa VNQwenPrompt para concatenar, nesta ordem: prefixo RGBA, descricao, pose, enquadramento, estilo, restricoes e sufixo RGBA. Prefixo/sufixo nao sao campos configuraveis do request de geracao. O estilo/enquadramento/restricoes continuam os mesmos de prompts.json; nao ha Prompt Extend.

Os prompts reais resultantes estao em `vn-final-concatenated-prompts.txt` e `vn-prompt-review.json`. Os textos foram produzidos pelo proprio no de concatenacao, nao montados manualmente para apresentacao.

Testes de contrato: 11 passaram. O dry-run completo usa o ComfyUI local, mocks apenas nas operacoes neurais, sem pesos, GPU, inferencia ou chamadas externas. Alem dos fixtures sinteticos, exercita os dois arquivos reais e as tres poses propostas, conferindo os textos que chegam ao encoder. Relatorio especifico: `vn-actual-request-dry-run.json`.

Nao houve publicacao desta revisao nem nova geracao paga. O job anterior e seus prompts completos permanecem documentados como historico em MODAL-RESULTS.md; nao foram reescritos.
