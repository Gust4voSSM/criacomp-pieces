# Charsheets GPT Image com os prompts originais

## Referências finais separadas

Usar `front.png` e `side.png`, ambos 1024 × 1536. Após a correção do autor, a lateral foi gerada novamente como imagem independente, com a frente GPT como referência. Para evitar as duas vistas na mesma saída, o prompt lateral foi adaptado: removida a instrução conflitante de frente, exigida uma única vista lateral e explicitados os detalhes visuais da nova frente. O texto final está em `side-separate-prompt.txt`. Portanto, somente a frente final mantém o prompt original sem alterações. `side-request-sheet.png` preserva a tentativa anterior e não deve ser usado como referência lateral final.

Ferramenta usada: image_gen integrada, sem seleção explícita de versão de modelo disponível na chamada.

Os prompts foram recuperados do grafo executado nos metadados do charsheet de frente original da segunda geração (refatorado-run), resolvendo StringConstantMultiline e StringConcatenate até os CLIPTextEncode de frente e lateral. Textos completos em `front-prompt.txt` e `side-prompt.txt`, sem acréscimos, remoções ou correções.

- `front.png`: nova geração somente por texto, sem referências visuais antigas.
- `side-request-sheet.png`: geração com o prompt lateral original e a nova frente GPT como referência visual, reproduzindo a dependência frente → lateral do workflow original. O modelo retornou uma folha com frente e lateral juntas, em vez de uma lateral isolada. O prompt original contém simultaneamente “front view” e “left side profile view”; essa contradição foi preservada para respeitar o teste de texto idêntico.

Ambos os arquivos são RGB de 1024 × 1536, com fundo preto. Não houve redimensionamento, geração de máscara, remoção de fundo ou edição posterior. As imagens são uma nova interpretação do texto, incluindo mudanças de uniforme, meias e calçados em relação às imagens FLUX.

Origem do prompt: https://raw.githubusercontent.com/Gust4voSSM/criacomp-pieces/main/experiments/vn-sprites-agentico/evidencias/refatorado-run/charsheet_front_00001_.png
