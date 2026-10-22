# Prompts das duas gerações

### Prompts da primeira geração

Textos gerados pelo agente e preservados nos metadados da primeira execução.

**Frente**

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid light grey background, soft even studio lighting, highly detailed
```

**Lateral**

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight, left side profile view, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid light grey background, soft even studio lighting, consistent character design
```

**Feliz**

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, cheerful happy smiling expression, waving one hand, friendly standing pose, visual novel sprite, flat anime cel shading, clean crisp lineart, plain solid light grey background, soft even studio lighting
```

**Surpresa**

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, surprised shocked expression, eyes wide open, both hands raised near chest, standing pose, visual novel sprite, flat anime cel shading, clean crisp lineart, plain solid light grey background, soft even studio lighting
```

**Tristeza**

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, sad teary crying expression, looking down slightly, hands clasped together in front, standing pose, visual novel sprite, flat anime cel shading, clean crisp lineart, plain solid light grey background, soft even studio lighting
```

### Textos usados na segunda geração

Após a refatoração, cada prompt é formado pelo texto compartilhado abaixo, seguido de vírgula e da especialização correspondente. As edições manuais relatadas pelo autor aparecem nesses textos.

**Texto compartilhado**

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid black background, soft even studio lighting, highly detailed
```

**Especialização — Frente**

```text
standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, full-body visual novel character reference, highly detailed
```

**Especialização — Lateral**

```text
standing straight, left side profile view, neutral calm expression, full-body visual novel character reference, consistent character design
```

**Especialização — Feliz**

```text
cheerful happy smiling expression, waving one hand, friendly standing pose, visual novel sprite
```

**Especialização — Surpresa**

```text
surprised shocked expression, eyes wide open, both hands raised near chest, standing pose, visual novel sprite
```

**Especialização — Tristeza**

```text
sad teary crying expression, looking down slightly, hands clasped together in front, standing pose, visual novel sprite
```

### Alterações visíveis entre os textos

- A descrição e o estilo passam a vir de um nó compartilhado.
- O fundo muda de “plain solid light grey background” para “plain solid black background”.
- Frente e lateral recebem “full-body visual novel character reference” nos textos específicos; antes tinham “visual novel character reference”.
- O texto compartilhado da segunda geração contém também a pose frontal e “highly detailed”. Essas instruções passam a integrar os cinco prompts concatenados.
- As instruções de felicidade, surpresa e tristeza continuam nos três textos específicos.

A refatoração foi solicitada ao agente em duas mensagens. O autor relatou a adição manual de “full-body” e as demais edições de texto para a segunda geração; os exports preservam os estados finais dessas edições.

## Antes/depois por prompt completo

## Frente

### Antes

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid light grey background, soft even studio lighting, highly detailed
```

### Depois — texto concatenado

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid black background, soft even studio lighting, highly detailed, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, full-body visual novel character reference, highly detailed
```

### Diferenças por segmento

```diff
--- primeira-geracao
+++ segunda-geracao
@@ -10,6 +10,12 @@
 visual novel character reference
 flat anime cel shading
 clean crisp lineart
-plain solid light grey background
+plain solid black background
 soft even studio lighting
 highly detailed
+standing straight facing the camera
+front view
+arms slightly away from body
+neutral calm expression
+full-body visual novel character reference
+highly detailed
```

## Lateral

### Antes

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight, left side profile view, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid light grey background, soft even studio lighting, consistent character design
```

### Depois — texto concatenado

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid black background, soft even studio lighting, highly detailed, standing straight, left side profile view, neutral calm expression, full-body visual novel character reference, consistent character design
```

### Diferenças por segmento

```diff
--- primeira-geracao
+++ segunda-geracao
@@ -3,12 +3,18 @@
 wearing a navy-blue sailor school uniform
 anime style
 full body
-standing straight
-left side profile view
+standing straight facing the camera
+front view
+arms slightly away from body
 neutral calm expression
 visual novel character reference
 flat anime cel shading
 clean crisp lineart
-plain solid light grey background
+plain solid black background
 soft even studio lighting
+highly detailed
+standing straight
+left side profile view
+neutral calm expression
+full-body visual novel character reference
 consistent character design
```

## Feliz

### Antes

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, cheerful happy smiling expression, waving one hand, friendly standing pose, visual novel sprite, flat anime cel shading, clean crisp lineart, plain solid light grey background, soft even studio lighting
```

### Depois — texto concatenado

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid black background, soft even studio lighting, highly detailed, cheerful happy smiling expression, waving one hand, friendly standing pose, visual novel sprite
```

### Diferenças por segmento

```diff
--- primeira-geracao
+++ segunda-geracao
@@ -3,11 +3,17 @@
 wearing a navy-blue sailor school uniform
 anime style
 full body
+standing straight facing the camera
+front view
+arms slightly away from body
+neutral calm expression
+visual novel character reference
+flat anime cel shading
+clean crisp lineart
+plain solid black background
+soft even studio lighting
+highly detailed
 cheerful happy smiling expression
 waving one hand
 friendly standing pose
 visual novel sprite
-flat anime cel shading
-clean crisp lineart
-plain solid light grey background
-soft even studio lighting
```

## Surpresa

### Antes

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, surprised shocked expression, eyes wide open, both hands raised near chest, standing pose, visual novel sprite, flat anime cel shading, clean crisp lineart, plain solid light grey background, soft even studio lighting
```

### Depois — texto concatenado

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid black background, soft even studio lighting, highly detailed, surprised shocked expression, eyes wide open, both hands raised near chest, standing pose, visual novel sprite
```

### Diferenças por segmento

```diff
--- primeira-geracao
+++ segunda-geracao
@@ -3,12 +3,18 @@
 wearing a navy-blue sailor school uniform
 anime style
 full body
+standing straight facing the camera
+front view
+arms slightly away from body
+neutral calm expression
+visual novel character reference
+flat anime cel shading
+clean crisp lineart
+plain solid black background
+soft even studio lighting
+highly detailed
 surprised shocked expression
 eyes wide open
 both hands raised near chest
 standing pose
 visual novel sprite
-flat anime cel shading
-clean crisp lineart
-plain solid light grey background
-soft even studio lighting
```

## Tristeza

### Antes

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, sad teary crying expression, looking down slightly, hands clasped together in front, standing pose, visual novel sprite, flat anime cel shading, clean crisp lineart, plain solid light grey background, soft even studio lighting
```

### Depois — texto concatenado

```text
a young woman with long silver hair in a side ponytail, violet eyes, wearing a navy-blue sailor school uniform, anime style, full body, standing straight facing the camera, front view, arms slightly away from body, neutral calm expression, visual novel character reference, flat anime cel shading, clean crisp lineart, plain solid black background, soft even studio lighting, highly detailed, sad teary crying expression, looking down slightly, hands clasped together in front, standing pose, visual novel sprite
```

### Diferenças por segmento

```diff
--- primeira-geracao
+++ segunda-geracao
@@ -3,12 +3,18 @@
 wearing a navy-blue sailor school uniform
 anime style
 full body
+standing straight facing the camera
+front view
+arms slightly away from body
+neutral calm expression
+visual novel character reference
+flat anime cel shading
+clean crisp lineart
+plain solid black background
+soft even studio lighting
+highly detailed
 sad teary crying expression
 looking down slightly
 hands clasped together in front
 standing pose
 visual novel sprite
-flat anime cel shading
-clean crisp lineart
-plain solid light grey background
-soft even studio lighting
```
