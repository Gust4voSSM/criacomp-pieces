# Execução real — descrição no upload e concatenação interna

Publicação autorizada e concluída em 23/10/2026. Job único: fc-01M5NCR7T6633YH0X518ZH5VQG. Qwen-Image-2.1 na Modal, referências externas frente e lateral separadas, com descrição geral persistida no mesmo conjunto. ID 61d2bfbcb43206a635023a5660305255a124e0db635ab23f22cae012d4f3a24e.

Três imagens concluídas em 123,619 s no runner, incluindo inicialização. RGBA nativo de 832 × 1248, alpha entre 0 e 255. 40 passos, CFG 1, Euler/simple, seeds speaking=12345, listening=23456, thinking=34567.

O request enviado tem somente reference_id e poses curtas. Os prompts completos foram reconstruídos diretamente dos nós VNQwenPrompt nos metadados dos PNGs reais e comparados byte a byte aos textos aprovados em vn-prompt-review.json: os três coincidem. O manifesto retornado no workflow também coincide com o upload, incluindo descrição e hashes das referências. Ver verification.json.

Inspeção visual: speaking produziu palma aberta na altura da cintura e boca aberta; listening manteve expressão calma e braços baixos; thinking colocou a mão sob o queixo e manteve o outro braço baixo. O olhar de thinking continua próximo da frente, apesar de solicitado levemente desviado. Inspecionadas composições em branco/cinza escuro e alpha isolado; isso não certifica cada fio e borda como recorte perfeito.

Originais sem pós-processamento em results/vn_qwen/. results.zip preserva PNGs, workflow, histórico e logs. three-poses.png é uma prévia sobre branco; preview-alpha.png acrescenta cinza escuro e alpha. Somente essas prévias foram redimensionadas, não os sprites entregues.
