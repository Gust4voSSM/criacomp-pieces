# Três poses VN com referências GPT separadas

API Modal atualizada em 23/10/2026 para aceitar POST /references e reference_id em POST /jobs, usando a adaptação existente validada em dry-run. Deploy: https://modal.com/apps/gssm/main/deployed/vn-sprites-qwen-image-21

Referências enviadas, nesta ordem: `front.png` e `side.png`. A imagem com duas vistas não foi enviada. Upload e manifesto retornado confirmam os mesmos hashes SHA256 dos arquivos locais, preservando os PNGs RGB 1024 × 1536.

Referência: 707694dc567549b7e1c2762e7e604c2c567083f8273589b8c7d52bd03e5e43a5

Job: fc-01M5NAPGF4NK89V0X1AVNJBV97

Um único job GPU concluído, três imagens; 121,646 s no runner incluindo inicialização. A tentativa anterior via modal run parou no cliente local por ausência de Pillow antes de upload/geração.

## Prompts e parâmetros

Os três prompts novos e completos estão em `vn-poses-request.json`. Não foram reutilizados os prompts antigos de feliz/aceno, surpresa ou tristeza. A API externa usa cada prompt literalmente, sem descrição compartilhada antiga e sem Prompt Extend. Os textos foram conferidos no workflow retornado.

- `speaking`, seed 12345: conversa acolhedora, sorriso discreto, boca ligeiramente aberta, uma palma aberta perto da cintura.
- `listening`, seed 23456: escuta atenta, boca fechada, braços relaxados nas laterais.
- `thinking`, seed 34567: reflexão, uma mão sob o queixo, olhar um pouco desviado.

Qwen-Image-2.1, alpha nativo, modo external_pair_speed, 40 passos, CFG 1, Euler/simple. Resolução de saída 832 × 1248, calculada pelo modo Speed a partir da proporção da segunda referência. Não houve redimensionamento ou tratamento de alpha nos PNGs entregues.

## Verificação e resultado

As três imagens são RGBA 832 × 1248, com alpha de 0 a 255. Manifesto de referências e prompts exatos foram confirmados no workflow do job. Inspeção visual sobre branco e cinza escuro, e alpha isolado, em `modal-poses-preview.png`. A prévia resumida `modal-three-poses.png` tem fundo branco só para visualização; os originais permanecem transparentes.

Os gestos principais saíram: palma na cintura para speaking, braços baixos para listening, mão no queixo para thinking. Em thinking, o outro braço ficou dobrado sustentando o cotovelo, embora o pedido fosse relaxado ao lado; o olhar também permanece próximo da frente. Há pequenas variações de proporção/expressão entre sprites. A inspeção não substitui validação manual de todas as bordas, dedos e fios.

Originais em `modal-results/vn_qwen/`. ZIP original em `modal-vn-poses.zip`, incluindo workflow, logs e resumo. Evidências: `modal-reference-manifest.json`, `modal-submitted-request.json`, `modal-job.json`, `modal-last-status.json` e `modal-verification.json`. Nenhuma credencial foi copiada para esses artefatos.
