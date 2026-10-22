# Execução inicial e execução após refatoração

A execução inicial corta as pernas. A posterior mostra o corpo inteiro, incluindo os sapatos. O autor acrescentou “full-body” aos textos específicos; o prompt já tinha uma ocorrência de “full body” que ele não havia percebido.

Antes: “visual novel character reference”
Depois: “full-body visual novel character reference”

O trecho está documentado nas especializações frontal e lateral. A hipótese de reforço permanece em aberto; o texto compartilhado e a cor de fundo também mudaram. Não foi identificado respaldo para atribuir o resultado especificamente ao hífen.

| Inicial — 20/10 | Posterior — 21/10 |
| --- | --- |
| Referência frontal<br>![Referência frontal inicial](evidencias/primeira-run/charsheet_front_00001_.png) | Referência frontal<br>![Referência frontal posterior](evidencias/refatorado-run/charsheet_front_00001_.png) |
| Referência lateral<br>![Referência lateral inicial](evidencias/primeira-run/charsheet_side_00001_.png) | Referência lateral<br>![Referência lateral posterior](evidencias/refatorado-run/charsheet_side_00001_.png) |
| Feliz / aceno<br>![Feliz / aceno inicial](evidencias/primeira-run/sprite_pose1_00001_.png) | Feliz / aceno<br>![Feliz / aceno posterior](evidencias/refatorado-run/sprite_00001_.png) |
| Surpresa<br>![Surpresa inicial](evidencias/primeira-run/sprite_pose2_00001_.png) | Surpresa<br>![Surpresa posterior](evidencias/refatorado-run/sprite_00002_.png) |
| Tristeza<br>![Tristeza inicial](evidencias/primeira-run/sprite_pose3_00001_.png) | Tristeza<br>![Tristeza posterior](evidencias/refatorado-run/sprite_00003_.png) |

## Workflows recuperados

- [Inicial](evidencias/primeira-run/charsheet_front_00001_.png.workflow.json): 60 nós e 93 conexões no canvas.
- [Refatorado executado](evidencias/refatorado-run/charsheet_front_00001_.png.workflow.json): 33 nós principais, incluindo três instâncias de um subgrafo de pose com 12 nós na definição.
- [Prompt executado após refatoração](evidencias/refatorado-run/charsheet_front_00001_.png.prompt.json).

A refatoração reúne a descrição da personagem e o estilo em uma fonte compartilhada, concatena os textos específicos e encapsula o ramo de pose para reutilizá-lo três vezes.

Os PNGs foram extraídos dos ZIPs sem edição. Proveniência e hashes estão nas pastas de cada execução.
