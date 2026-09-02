# WAY Brandbook — Proyecto

## ¿Qué es WAY?

Marca de moda femenina peruana. Canal principal ecommerce con tienda física.

| Dato | Valor |
|---|---|
| Web | https://wayperuvian.pe/ |
| Instagram | @way_peruvian |
| TikTok | @way_peruvian |
| Tienda física | Galería Damero, Lima, Perú |
| Ecommerce | Shopify |
| Atención al cliente | WhatsApp Business (sistema way-inbox) |
| Categorías principales | Blusas, vestidos, sets, bodys, abrigos, blazers, chaquetas, chalecos, faldas, pantalones, tops |
| Diferenciador operativo | Envíos en 24 horas |
| Diferenciador de producto | Producción por lotes pequeños — inicia en 50 unidades, máx. ~200, sin reposición. Renovación constante de catálogo, exclusividad real ("no se vea ni al costado"). **Esto aplica a las prendas, no al empaque** — el empaque (bolsas, hang tags, etc.) normalmente se compra al por mayor, aparte del ritmo de producción de ropa (error que se cometió una vez en `brandbook.html`, corregido — ver Notas Técnicas — Empaque) |

---

## ⚠️ Estado Actual / Pendiente Inmediato

Leer esto primero — es lo que cambió más recientemente y lo que hay que resolver antes de seguir avanzando:

- **`brandbook.html` ya no tiene ningún bloqueante de contenido pendiente de la clienta.** Misión y Visión se cerraron el 19/08 (Lizzie dio su alcance por audio — crecimiento nacional/tiendas ancla para Visión, moda moderna + seguridad/confianza de la clienta para Misión — se redactó una propuesta y la aprobó sin cambios) y el diseño/dirección de Empaque también quedó validado el mismo día. Junto con el tagline **"Con nombre propio"** (ya cerrado antes), toda la identidad — visual y de contenido — está aprobada por la clienta.
- **Repo sincronizado y pusheado.** `git push` hecho el 19/08 (`4f99d46..a8b4621`), GitHub Pages al día con los cambios de Misión/Visión. Sigue aplicando la norma general para el futuro: **confirmar con Juan antes de cada `git push`.**
- **Cotización aprobada y facturación en curso:** monto final **S/6,500**, 50% ya pagado, 50% restante al finalizar el proyecto. `propuesta-economica-v3.html` es el documento que se aprobó.
- **Empaque:** diseño/dirección validado por la clienta. Cotización real de proveedor y fecha de producción quedan **fuera del alcance de este proyecto** (decisión de Juan, 19/08) — no son un pendiente abierto del brandbook.
- **`assets/logo/logo.webp` (logo legacy):** ✅ documentado como identidad "antes" — insertado en `estrategia-lanzamiento.html` (sección Transición de Assets, comparativo antes/después con el wordmark nuevo), confirmado visualmente con Juan antes de commitear. Ver Archivos del Proyecto.
- **`estrategia-lanzamiento.html` sigue en iteración activa** — no tratarlo como cerrado. Objetivo explícito del cliente: que la calidad esté a la altura del resto del proyecto, y que quede lo más ejecutable posible para no recargar de trabajo a quienes lo van a llevar a cabo (Lizzie y el/la community manager). **Sección "08 — Riesgos y Contingencias" removida por completo (19/08)** — Juan pidió más flexibilidad: el proyecto no debe retrasar el rebranding por el empaque físico (cotización/producción, fuera de alcance). La única fila con contenido no duplicado (protocolo de reacción negativa de la comunidad) ya vive en `guia-instagram.html`, así que no se perdió nada al quitarla. Fase 0 ("✓ Estado actual") y Fase 4 ("Transición de Assets" — fila de empaque) se reescribieron con la misma lógica: el Día D se calendariza sin esperar al empaque definitivo, usando empaque transicional/genérico (sin el logo anterior) como puente si hace falta.
- Recomendación de limpieza que quedó **sin decidir**: si vale la pena reorganizar la raíz del repo (ver "Próximos Pasos").
- **`entrega-cliente/` construida y pusheada (24–25/08)** — carpetería completa de assets para la encargada de marketing (logo en todos los formatos, tipografías con itálica real, colores, 6 piezas de empaque + etiqueta tejida por talla, `LEEME.pdf`). Sticker de Sellado confirmado por Juan sin cambios. `git push` hecho el 25/08 (`69f19fd..4998892`), GitHub Pages al día. Ver Notas Técnicas — Carpeta de Entrega para el detalle, incluido un hallazgo de seguridad en la herramienta MCP de Playwright (no en esta máquina) que hay que tener presente en sesiones futuras.

---

## Estado del Proyecto (Agosto 2026)

| Fase | Entregable | Estado |
|---|---|---|
| 1 | Análisis de marca + 3 territorios propuestos | ✅ Completado |
| 2 | Propuesta de identidad visual (paletas, logos, tipografías) | ✅ Completado |
| 3 | Propuestas de logo/identidad en Claude Design | ✅ Completado |
| 4 | Aprobación de territorio + identidad por cliente | ✅ Completado — La Firma |
| 5 | Brandbook completo (`brandbook.html`) | ✅ Construido y hosteado (v1.1+), pusheado y al día — cotización aprobada, tagline, misión/visión y empaque cerrados |
| 6 | Guía de Instagram (`guia-instagram.html`) — documento operativo separado | ✅ Construido |
| 7 | Guía de Ecommerce (`guia-ecommerce.html`) — documento operativo separado | ✅ Construido |

---

## Decisiones Confirmadas por el Cliente

- **Territorio elegido:** LA FIRMA — WAY como nombre con autoridad ganada, solo tipografía sin símbolos
- **Tagline:** ✅ **"Con nombre propio"** — elegido por la clienta entre 5 opciones ("Hecha a tu manera" / "Una manera propia" / "Con nombre propio" / "Tu estilo. Tu firma." / "El nombre lo dice todo"). Actualizado en todo `brandbook.html`.
- **Audiencia confirmada:** Mujer 28–65+, independiente económicamente, socialmente activa
- **Ticket promedio confirmado:** S/180
- **Logo / Paleta / Tipografía:** Definidos por territorio La Firma (ver sección de identidad visual y Notas Técnicas)
- **Monograma:** Recto (no itálico) — confirmado por la clienta, ver Notas Técnicas
- **Marca competidora / referencia:** Saint Male (@saintmale.cl — Chile)
- **Estilo fotográfico:** Definido (ver sección de fotografía)

---

## Identidad de Marca

### Territorio: NOSOTRAS
Lo que Glossier hizo por la belleza, aplicado a la moda premium accesible en América Latina.
La marca se construye *con* sus clientas, no se les dirige desde arriba.

### Brand DNA — 8 atributos
1. **Cálida** — emocionalmente presente, no distante
2. **Segura** — autoridad ganada, no actuada
3. **Comunidad primero** — construida juntas, de todas
4. **Atemporal** — relevante en 2026 y en 2036
5. **Premium accesible** — aspiracional sin excluir
6. **Alma peruana** — con raíces, no folclórica
7. **Editorial** — curada e intencional
8. **Íntima** — una amiga de confianza con gusto impecable

### Tono de Voz
- **Sí:** Emojis naturales (✨😍), segunda persona (tú), verbos de acción, cercanía
- **No:** Lenguaje corporativo, tecnicismos, condescendencia
- **Voz:** Amiga que da consejos de moda, no vendedora agresiva

### Copy existente de referencia
- "Tu combinación perfecta la encuentras aquí ✨"
- "Luce única con nosotras"
- "Ropa de moda para la mujer empoderada"
- "ENVÍOS EN 24 HORAS"

---

## Audiencia Objetivo

- **Género:** Mujer
- **Ubicación:** Lima, Perú (expansión nacional)
- **Edad confirmada:** 28–65+ (corrección del cliente; rango real más amplio que el inicial)
- **Psicografía:** Activa, socialmente conectada, guiada por valores, valora el gusto y la experiencia
- **Comportamiento:** Descubre en Instagram, consulta por WhatsApp antes de comprar, valora envío rápido
- **Canal principal:** WhatsApp + Instagram (más que TikTok, dado el rango de edad real)
- **Ticket promedio:** ✅ S/180
- **Posicionamiento de precio:** Mid-range accesible `[PENDIENTE — confirmar]`

---

## Territorios Creativos Explorados

Tres territorios desarrollados en Claude Design. El cliente ya eligió — **Territorio 01, La Firma** — los otros dos quedan solo como contexto histórico de por qué se descartaron (ya no son decisiones activas).

### Territorio 01 — La Firma ✅ ELEGIDO
- **Concepto:** WAY como nombre con autoridad ganada. Solo tipografía, sin símbolos (como ZARA, PRADA, CELINE)
- **Tipografía:** Bodoni Moda — serif didona de alto contraste
- **Paleta:** Marfil cálido `#F7F3EE` · Casi negro `#2A1F18` · Terracota `#C4714A`
- **Monograma:** W recta en círculo oscuro (para avatar 110px) — ver Notas Técnicas para el porqué del cambio de itálica a recta
- **Fortaleza:** Atemporalidad, percepción premium más alta
- **Consideración:** Escalabilidad (trazos finos en bordado requieren versión engrosada)

### Territorio 02 — El Encuentro *(descartado)*
WAY como lugar donde todas las mujeres se encuentran, minúscula = igualdad sin jerarquía. Nunito Sans 800, paleta rosa/lavanda, símbolo de arco abierto. Más fácil de escalar/bordar que La Firma, pero con riesgo de datarse (estética de calidez muy de tendencia).

### Territorio 03 — La Arquitecta *(descartado)*
WAY como mujer que construyó su camino con método (referencias COS, Massimo Dutti). Archivo 600, paleta hueso/bronce, la "Λ" (A sin barra) como elemento distintivo. El más sofisticado y editorial, pero requería que el cliente entendiera la letra modificada — más difícil de explicar.

### Documento de propuesta en Claude Design
- **Project ID:** `9dbd8d48-5534-4de1-a638-c49f9e2d1217`
- **Archivo:** `WAY Brand Identity Territories.dc.html`
- **Contenido:** Portada · Fundamento Estratégico · Principios de Diseño · Requisitos Funcionales · 3 Territorios (paleta + sistema de identidad + tipografía + aplicaciones + evaluación) · Comparación directa · Cierre
- **Protecciones:** Marca de agua "PROPUESTA PRELIMINAR" · Disclaimer de confidencialidad · Footer con aviso de acuerdo comercial
- **Idioma:** Español

---

## Cómo Trabajar con Juan

Patrones de colaboración que se establecieron en la sesión de ajuste del logo — mantenerlos en sesiones futuras:

- **Nunca aplicar un cambio de diseño a la identidad ya aprobada sin mostrarlo primero.** El flujo que funciona: generar un comparativo visual (render + captura de pantalla, o un Artifact privado si es para mandarle a la clienta) y esperar confirmación antes de tocar los archivos de producción.
- **Los ajustes de diseño se hacen de a poco**, no en saltos grandes — Juan lo pidió explícitamente al bajar el contraste del wordmark (paso a paso: 30 → 20 → 16, no directo a un valor bajo). Aplica a cualquier ajuste futuro de tipografía/color/espaciado.
- **No asumir que una crítica de la clienta implica rediseñar.** Diagnosticar primero si el problema es real o un artefacto — ej. el aro de colores de Instagram (nativo de la plataforma, no del logo) o un bug de contraste en modo oscuro de un comparativo que hizo parecer que dos versiones se veían "iguales" cuando en realidad ninguna se veía.
- **Mensajes que Juan le redacta a Lizzie** (tienen confianza, se tutean): primer párrafo optimista pero sin entrar en detalle específico todavía; validar explícitamente que sus observaciones sí sirvieron para mejorar el brandbook, sin sonar corporativo. Prefiere "se solicitó" sobre "nos pediste" cuando quiere un framing menos personal/directo.
- **Antes de compartir algo con la clienta**, Juan revisa y pide ajustes de tono — no enviar directo.

---

## Notas Técnicas — Pipeline del Wordmark

**Importante para cualquier sesión futura que toque el logo:** el pipeline de regeneración vivió en el scratchpad de la sesión anterior, que no persiste — hay que reconstruirlo desde este resumen si hace falta tocar el wordmark otra vez.

### Por qué no usar fontTools directo
Instanciar Bodoni Moda (`wght`/`opsz`) con `fontTools.varLib.instancer` produce contornos autointersectados/rotos en ciertas combinaciones de ejes — confirmado varias veces, no es un caso aislado. Ni siquiera `removeOverlaps` de `skia-pathops` lo arregla (el problema es de datos, no de topología/solapamiento).

### Método que sí funciona
1. Renderizar el texto en un navegador real (Playwright/Chromium), forzando `font-variation-settings: 'opsz' N` vía CSS al valor deseado, a resolución alta (ej. `font-size: 1600px`).
2. Capturar como PNG de alta resolución.
3. Vectorizar con OpenCV: `cv2.findContours` + `cv2.approxPolyDP`, generando el SVG con `fill-rule="evenodd"`.

El navegador instancia la fuente variable correctamente — el bug está solo en el lado de fontTools/gvar.

### Fuentes usadas
`BodoniModa.ttf` y `BodoniModa-Italic.ttf` (variable), descargadas del repo `google/fonts` en GitHub, carpeta `ofl/bodonimoda`. **Bodoni Moda no tiene eje `ital`** — la itálica es un archivo aparte, no un valor de eje.

### Calibración final del wordmark
- `wght 400` — es el mínimo del eje, no se puede bajar más dentro de esta tipografía.
- `opsz 16` — recorrido con la clienta: 96 (máximo técnico, pedido inicial comparando con ZARA) → 30 (96 se veía demasiado frágil) → 20 (pedido de adelgazar el trazo grueso; el cambio no se notaba bien a simple vista en el comparativo) → **16, valor final confirmado por Lizzie**. Para que el cambio del trazo grueso se viera con claridad en el comparativo, además de los renders normales se usó una superposición de contornos (versión vieja en outline sobre la nueva en relleno) y un acercamiento a una sola letra — comparar dos wordmarks completos a tamaño normal no bastaba, el ojo se va al hairline porque ahí el cambio relativo es mucho mayor.
- **Si en el futuro piden un trazo aún más delgado:** no hay más margen en Bodoni Moda (wght ya en el piso). Las opciones son cambiar de tipografía (probable costo de licencia, revisita la decisión de Territorio 01) o edición manual del vector (no recomendado — rompe el sistema paramétrico que permite regenerar todo consistentemente). Ya se conversó esto con Juan, la preferencia es explorar tipografía antes que edición manual.
- `way-wordmark-embroidery-master.svg` **nunca se toca** en estos ajustes — peso 800 fijo, requisito técnico del bordado, independiente del wordmark digital.

### Monograma: itálica → recta
Se le presentó a la clienta un comparativo (itálica actual vs. recta, a escala real de avatar 32–110px) con recomendación hacia recta. Lizzie eligió recta. Aplicado en `way-monogram.svg`, `favicon.png`, `way-monogram-180.png`, y en los monogramas de texto CSS de los cuatro documentos (ver siguiente sección) — se quita `font-style: italic` de las reglas `.portada-monogram span`, `.ig-avatar span`, `.wa-avatar span`.

### ⚠️ El wordmark vive en 4 archivos, no solo en `brandbook.html`
`guia-instagram.html`, `guia-ecommerce.html` y `estrategia-lanzamiento.html` tienen **su propio CSS de wordmark/monograma** (`.wordmark`, `.sidebar-brand`, y en `estrategia-lanzamiento.html` también los monogramas de texto), copiado en algún punto anterior y completamente independiente del de `brandbook.html`. Se sincronizaron una vez en esta sesión (estaban en peso 500 / tracking `.3em`/`.28em` / sin `opsz`, el estado pre-sesión). **Cualquier cambio futuro al wordmark debe replicarse en los cuatro archivos** o van a volver a desincronizarse.

### AI/EPS del wordmark — resuelto sin Illustrator (PDF vectorial)
Juan no tiene Illustrator. En vez de bloquear el punto "AI/EPS" (pendiente #10), se generó un **PDF vectorial real** directo desde los SVG ya aprobados, con la librería Python `cairosvg` (`pip install cairosvg`, luego `cairosvg.svg2pdf(url=..., write_to=...)`) — conversión de segundos, sin dependencias pesadas ni Ghostscript/Inkscape. Se generaron `way-wordmark-negro.pdf`, `way-wordmark-marfil.pdf` y `way-monogram.pdf` en `assets/logo/`.

Un PDF vectorial es **funcionalmente equivalente a un AI/EPS** para producción de imprenta — el propio formato `.ai` de Illustrator es internamente PDF desde las versiones CS, y la mayoría de imprentas en Lima aceptan PDF vectorial sin problema (muchas hoy lo prefieren sobre EPS, que es un formato más antiguo). Si algún proveedor puntual exige específicamente `.ai` o `.eps` y no acepta PDF, recién ahí vale la pena reabrir este punto — mientras tanto no es un bloqueante. `way-wordmark-embroidery-master.svg` queda fuera de este método — el archivo de bordado (DST/PES) sigue siendo un pendiente real, aparte, que solo puede generar un proveedor de bordado.

---

## Notas Técnicas — Empaque (conceptos "Después")

Al generar los primeros 7 conceptos de empaque con Nano Banana a partir de prompts de solo texto, ninguno sirvió: la IA no reproduce la tipografía/logo exacto de WAY (mismo problema de fondo que motivó el pipeline de renderizado en navegador para el wordmark digital, ver arriba), además de fallas específicas — proporciones poco realistas para ropa, sin info de marca, sticker de sello de cera no factible en lotes de 50-200, tarjeta de agradecimiento con copy pobre, caja genérica.

**Corrección aplicada (segunda vuelta):**
- **Referencias adjuntas, no solo descritas:** Nano Banana sí soporta adjuntar imágenes de referencia — se adjunta `way-wordmark-marfil-sobre-negro.png` o `way-monogram-180.png` como referencia tipográfica exacta, y una foto real (`empaque-antes-*.jpeg` para proporción de bolsa, `pieza-sola.jpg` para prenda real en el tissue paper) en vez de describir todo solo en texto.
- **Hang tag y tarjeta de agradecimiento ya no se generan con IA** — se resolvieron como componentes CSS reutilizando el `.hangtag` ya aprobado y un `.thankyou-card` nuevo, con copy redactado en el tono de voz de marca. Tipografía garantizada, cero riesgo de reinterpretación.
- **Sin número de WhatsApp impreso en empaque** — decisión explícita de Juan: el número puede cambiar y reimprimir empaque físico por eso no es viable; se usa `@way_peruvian · wayperuvian.pe` en su lugar (información que sí se mantiene actualizada sin reimprimir nada).
- **Sticker de sellado:** se reemplazó el concepto de sello de cera por un sticker plano impreso a 1 tinta (factible con cualquier imprenta de stickers en Lima).
- Bolsa (2 direcciones: kraft y negra elevada), tissue paper, sticker y caja de envío: generados con los prompts corregidos y ya integrados en `brandbook.html` (`assets/photos/empaque-despues-*.png`). Dos rondas de ajuste necesarias: la primera con caja en formato panorámico (le faltaba especificar aspect ratio 4:5 en el prompt) y tissue paper con una prenda distinta a la esperada (resuelto — Juan decidió usar otra prenda WAY a propósito, no fue error). Sistema completo con concepto de dirección para las 6 piezas, pendiente de validación final de la clienta antes de producción.

**Revisión "Físico — Escala Real" → fin del documento (12/08):** se corrigieron varias inconsistencias — título "Piezas a Definir" contradecía el "resuelto" de hang tag/tarjeta (renombrado a "Sistema de Empaque"), el tagline "una manera propia" aparecía sin marca de pendiente en el hang tag (agregada, y solo hace falta en un lugar ahora porque el hang tag reutilizado en "Sistema de Empaque" muestra el dorso en vez de repetir el frente), grid de "Antes" tenía 2 fotos duplicadas de la misma bolsa kraft (bajado de 4 a 3), y un bug real de responsive (un `style` inline le ganaba a la regla de mobile — reemplazado por clases `.pack-photo-grid--2col`/`--3col`).

**Ampliación de la sección (13/08):** a pedido de Juan, se agregó (1) tercera dirección de bolsa en "Después"; (2) tabla **"Elegir la Bolsa"** (costo relativo estimado y mejor uso por formato — costos son estimados, no cotización real, marcado como pendiente); (3) bloque **"Lineamientos de Producción"** (color HEX con nota de conversión a CMYK/Pantone pendiente, tipografía siempre vectorial, tamaño mínimo impreso pendiente de confirmar con proveedor, filtro de lotes 50-200, checklist pre-producción); (4) tabla **"Aplicación del Logo en Empaque — Qué Sí / Qué No"**, mismo patrón que "Usos Incorrectos" del logo pero para contexto de producción física.

**Sobre la 3ra dirección de bolsa — ojo con la confusión de nombres:** Juan generó primero una **bolsa blanca de papel** (buena calidad, aprobada visualmente) pero nunca llegó a guardarla como archivo — solo existió pegada en el chat, se perdió al no tener yo forma de extraer imágenes pegadas directamente a disco. Después aclaró que en realidad quería la **bolsa plástica** (la segunda foto de "Antes", `empaque-antes-2.jpeg`) como prioridad. Esa sí se generó, se ajustó una vez (primera versión muy translúcida, dejaba ver la prenda de adentro y rompía consistencia con el resto del set — se pidió opaca y vacía) y quedó guardada como `assets/photos/empaque-despues-bolsa-c.jpg` (llegó en `.jfif`, renombrada a `.jpg`). **Las 3 direcciones "Después" hoy son: kraft, negra, plástica** — no incluye blanca. **Decisión (13/08, no solo pendiente):** no se va a agregar blanca como 4ta variante — kraft y plástica ya cubren la evolución de bajo costo de lo que existe hoy, una 4ta opción no abre una decisión nueva, solo alarga la sección. Si en el futuro se reconsidera, el prompt queda documentado más abajo en esta nota (histórico).

**Riesgo de factibilidad de la bolsa negra mate:** Juan notó que probablemente sea difícil/costosa de producir — válido: tinta clara sobre bolsa negra normalmente requiere foil o tinta blanca de base, procesos especializados con mínimos de producción más altos, mismo tipo de riesgo que ya descartó el sello de cera. Se agregó esta advertencia a la tabla "Elegir la Bolsa" en `brandbook.html` — la negra queda marcada como la opción que necesita validar factibilidad en lote de 50–200 antes de tomarla en serio, no como una alternativa igual de viable que kraft/plástica.

**Limpieza de "Lineamientos de Producción" (13/08):**
- Se quitaron referencias visibles al propio proceso de generación con IA (ej. "el mismo problema que tuvimos generando conceptos con IA" en la fila de Tipografía) — ese tipo de comentario es razonamiento interno de la sesión, no contenido para el brandbook. Se revisó todo el documento buscando frases similares ("ya aplicado", "ya descartó" referidas al sello de cera) y se reescribieron para que citen la regla/precedente sin narrar el historial de edición.
- El dato "WAY produce en lotes de 50–200 unidades" está confirmado — viene del diferenciador de producto capturado al inicio de este archivo, y el concepto general ("lotes pequeños, sin reposición") ya aparecía antes en `brandbook.html` (intro de "Quiénes somos" y valor de marca "Exclusividad"), pero el número exacto (50–200) solo se explicitaba en Empaque, y ahí estaba repetido casi textual 3 veces seguidas. Se dejó explicado una sola vez (fila "Lotes pequeños" en Lineamientos) y las otras 2 apariciones ahora son referencias cortas a esa fila.
- Se agregó una conversión aproximada HEX→CMYK (cálculo directo, no cotización de proveedor) para los 3 colores de marca, como punto de partida en vez de dejar el pendiente completamente vacío — la nota de pendiente ahora es más específica: el proveedor debe ajustar por su perfil de color y sustrato, no partir de cero.
- El checklist pre-producción pasó de un párrafo con signos de interrogación seguidos a una lista real dentro de un `pending-block` (mismo componente ya usado para otros pendientes del documento) — es información que se va a usar activamente, no una nota de pie de página.

**Orden de las galerías Antes/Después:** a Juan le generó confusión ver 3 fotos vs. 3 fotos sin que las posiciones correspondieran (parecía que la negra "reemplazaba" a la blanca). Se reordenaron ambas galerías para alinear lo que sí tiene equivalencia directa: posición 1 = kraft/kraft, posición 2 = plástica/plástica opaca; posición 3 queda blanca (antes, sin versión "después" todavía) junto a negra (después, dirección adicional sin equivalente en "antes") — con una nota explícita aclarando que no es una sustitución 1:1. Mismo criterio aplicado en la tabla "Elegir la Bolsa" (reordenada kraft/plástica/negra, con la negra marcada como "adicional, sin equivalente hoy").

**Corrección importante — "lotes pequeños" no aplica al empaque (13/08):** desde el primer intento de generar conceptos de empaque, se venía asumiendo que cualquier pieza de empaque debía ser "rentable en un lote de 50–200 unidades" (el mismo número que el diferenciador de producción de **ropa**). Juan corrigió: las prendas sí se producen en lotes chicos sin reposición, pero **el empaque normalmente se compra al por mayor, aparte** — no tiene sentido evaluar factibilidad de una bolsa o sticker contra el tamaño de lote de las prendas. Se corrigió en varios lugares de `brandbook.html`:
- Fila "Lotes pequeños" en Lineamientos de Producción → renombrada "Volumen de compra". Juan pidió después quitar esa fila por completo (no solo corregirla) — se removió de `brandbook.html`. La corrección de fondo (empaque y ropa se compran en ritmos distintos) queda documentada aquí y en la tabla "¿Qué es WAY?" al inicio de este archivo, por si hace falta retomarla.
- Tabla "Aplicación del Logo en Empaque": la fila "Procesos rentables solo en tirajes grandes (sellos de cera, foil complejo)" no tenía sentido con la lógica corregida (tirajes grandes ya no son necesariamente el problema) y además a Juan no le quedaba clara — se reemplazó por "Sellado manual pieza por pieza (ej. sello de cera)", con la razón real: no escala con el despacho diario y es frágil en envío.
- Tabla "Elegir la Bolsa" y checklist pre-producción: se quitaron las referencias a "lote de 50–200" aplicadas al empaque.
- Se agregó una aclaración en la tabla de "¿Qué es WAY?" al inicio de este archivo, en la fila del diferenciador de producto, para que quede claro desde el origen del dato que aplica a prendas, no a empaque.

**También en esta ronda:**
- **Proporción del wordmark en bolsa impresa:** Juan pidió alguna referencia de tamaño mínimo aunque no haya cotización de proveedor. Se agregó una proporción basada en los conceptos ya generados (wordmark ocupa 40–45% del ancho de la bolsa, no bajar de ~25%) como punto de partida, sin cerrar el pendiente de confirmación real con proveedor.
- **Costo relativo de las bolsas:** Juan pidió omitirlo — se quitó la columna "Costo relativo" de la tabla "Elegir la Bolsa" (esos valores eran estimados, no cotizados). Se mantuvo la advertencia técnica sobre la negra mate (foil/tinta blanca de base) porque es un hecho de proceso de impresión, no una cifra de costo inventada.
- **Texto de la bolsa blanca:** decía "todavía no tiene una versión Después generada", lo cual sonaba a pendiente cuando en realidad ya se decidió no generarla — corregido para reflejar que es una decisión tomada, no un pendiente.
- **Zona de Exclusión:** Juan confirmó los valores (80px digital / 1.5cm bordado) como definitivos — se quitó el flag `[PENDIENTE — confirmar con diseñador]`.
- **Estadísticas de TikTok:** Juan compartió la URL y una captura del perfil real (@way_peruvian) — actualizado en `brandbook.html` con cifras reales: 22 siguiendo, 23,9 mil seguidores, 115,8 mil me gusta (antes eran ilustrativas: 626/18,4 mil/142,3 mil). Las reproducciones por video individual siguen siendo ilustrativas. También se corrigió una frase de la intro que decía "hoy no tiene mockup en el brandbook" — sí lo tiene, justo debajo.
- **Tagline confirmado por la clienta: "Con nombre propio"** — reemplazado en todo `brandbook.html` (portada, sección Logo, Tipografía, jerarquía tipográfica, hang tag) y quitados todos los flags `[PENDIENTE — selección final de tagline]`. También se actualizó el "Estado actual" de `estrategia-lanzamiento.html` (acuerdo comercial y tagline ya no figuran como abiertos, solo queda empaque físico pendiente de aprobación final).
- **Misión y Visión — cerradas (19/08):** Lizzie dio su alcance por audio transcrito, con dos ideas mezcladas bajo "visión" que en realidad correspondían a las dos tarjetas distintas: (1) crecimiento — liderazgo a nivel nacional, tiendas propias y presencia en tiendas ancla, con un salto siguiente a ser referencia en América Latina (esto sí es Visión); (2) experiencia de la clienta — moda actual, seguridad y confianza al vestir, transmitir modernidad sin importar la edad (esto es Misión, aunque ella lo mencionó hablando de visión). Se separaron ambas ideas en su tarjeta correspondiente. Un punto de la transcripción decía "no ser líderes a nivel nacional" — interpretado como artefacto de transcripción (probable "no sé si...") dado que el resto del audio describe expansión, no lo contrario; se redactó como afirmación positiva ("ser líderes"), no como negación. También mencionó un posible plazo ("de acá a 5 años") pero dudando si correspondía — se dejó fuera del texto de la Visión a propósito, porque una visión de marca se redacta atemporal (mismo criterio que el atributo de marca "Atemporal"); si se quiere fijar un horizonte de tiempo concreto, debería vivir como meta en `estrategia-lanzamiento.html`, no en la tarjeta de Visión. Lizzie aprobó el borrador propuesto sin cambios — actualizado en `brandbook.html` y removido el `pending-block` que marcaba Misión/Visión como sin confirmar.

---

## Notas Técnicas — Carpeta de Entrega (`entrega-cliente/`)

Carpeta nueva (24/08) con todos los assets de marca organizados para que la encargada de marketing de WAY los use sin depender de Illustrator. Estructura: `01-Logo/` (vectorial + PNG transparente + JPG fondo sólido + guía de uso), `02-Tipografia/` (Bodoni Moda + Archivo, variables, oficiales de Google Fonts con licencia OFL — **no** instanciadas con fontTools, mismo bug de contornos rotos que ya se documentó para el wordmark), `03-Colores/`, `04-Empaque/` (una subcarpeta por pieza) y `05-Documentos-de-Marca/` (brandbook + 2 guías en PDF). Índice: **`LEEME.pdf`** (25/08 — empezó como `LEEME.md`, pero Juan hizo notar que la clienta probablemente no tiene con qué abrir Markdown formateado; se convirtió a PDF con el mismo template de marca que las demás guías, y se borró el `.md` para no dejar dos "léeme" distintos en la carpeta).

**Qué quedó vectorizado (listo para imprenta) vs. qué quedó como referencia:** Hang Tag (frente/dorso) y Tarjeta de Agradecimiento se exportaron a PDF/SVG real a partir del CSS ya aprobado en `brandbook.html` (`.hangtag`, `.thankyou-card`) — texto seleccionable, no imagen. El Sticker de Sellado es una pieza nueva (no existía como componente CSS, solo como foto concepto de IA) construida reutilizando el `way-monogram.svg` ya aprobado como sticker circular de 1 tinta — se le mostró a Juan antes de incluirlo por ser la única pieza nueva de este lote (no una re-exportación de algo ya aprobado); **confirmado sin cambios el 25/08.** Bolsa, tissue paper y caja de envío **se quedaron como imagen concepto + ficha técnica**, no como archivo de producción — su forma real depende 100% del troquel/máquina del proveedor, que sigue fuera de alcance del proyecto (ver Empaque más abajo). Cada pieza de `04-Empaque/` tiene su propia `Ficha-Tecnica-*.pdf` con colores/tipografía/copy/proporciones extraídos del brandbook, no inventados.

**⚠️ Incidente de seguridad — herramienta MCP de Playwright, no reproducible en Playwright local:** al generar los primeros PDF con la herramienta de navegador del harness (`mcp__playwright__*`), 2 de 3 archivos salieron con contenido inyectado que el HTML fuente nunca tuvo — un overlay tipo anuncio ("Join Discord Community" / "Get Premium FREE" / etc.) con un link real embebido (`https://discord.gg/...`), confirmado con PyMuPDF (no era un glitch visual, el link quedaba como anotación clicable dentro del PDF). Reiniciar esa sesión de navegador **no** lo resolvió — volvió a pasar de inmediato en un archivo distinto. Se aisló la causa: es específico de la sesión de navegador de esa herramienta MCP (posiblemente compartida/remota), no de esta máquina ni de Playwright en sí — un Chromium lanzado localmente vía el paquete Python `playwright` (`pip install playwright`, ya instalado en este entorno) salió limpio en todas las pruebas. **Regla para cualquier sesión futura: no usar `mcp__playwright__*` para generar archivos de entrega/producción** (sí sirve para exploración visual rápida, capturas de pantalla de bajo riesgo). Usar en su lugar Python `playwright` local + verificación posterior con PyMuPDF (`page.get_links()` no debe tener URLs inesperadas, `page.get_text()` no debe tener texto que el HTML fuente no tenga) antes de aceptar cualquier PDF como final — el patrón completo (generar, verificar con una librería independiente, recién entonces aceptar) queda en `entrega-cliente/` como el flujo a repetir. Los 3 PDF contaminados se borraron sin abrir el link ni interactuar con él.

**Causa raíz encontrada y corregida (27/08):** el mismo overlay volvió a aparecer en una sesión posterior (proyecto `way-shopify-lanzamiento`, verificando el preview local del tema de Shopify) — esta vez se rastreó hasta `.mcp.json` en la raíz de este repo, que apuntaba a `playwright-mcp` **sin scope**, un paquete de terceros (autor individual, `qaby.ai`) que incluye `posthog-node` (telemetría) entre sus dependencias — no el paquete oficial de Microsoft (`@playwright/mcp`). Ese paquete injectaba el overlay en cualquier página renderizada a través de él, sin importar el sitio. Corregido: `.mcp.json` ahora apunta a `@playwright/mcp@latest` (oficial, `github.com/microsoft/playwright-mcp`). **Como `.mcp.json` está commiteado, cualquiera que clonara este repo heredaba el paquete comprometido** — este fix aplica para todos. La regla de arriba (preferir Playwright local para archivos de entrega) sigue vigente igual, ahora con la causa raíz documentada.

**Itálica real, no falsa:** el primer intento solo descargó el archivo variable "normal" de cada tipografía. Ambas familias usan itálica en el brandbook (Bodoni Moda en taglines/citas/mensaje de la tarjeta; Archivo en notas aclaratorias como `.clearspace-note`) — y en ninguna de las dos la itálica es un eje dentro del archivo normal, es **un archivo `-Italic` completamente aparte** (mismo patrón ya documentado para Bodoni Moda en Notas Técnicas — Pipeline del Wordmark, confirmado que también aplica a Archivo). Sin ese archivo, el navegador sintetiza una itálica falsa (inclina el glyph normal) — pasó exactamente eso en la primera versión de `tarjeta-agradecimiento.pdf`. Se agregaron `BodoniModa-Italic-Variable.ttf` y `Archivo-Italic-Variable.ttf` a `02-Tipografia/` y se regeneró la tarjeta con la itálica real embebida.

**Nombres de instancia vs. `opsz` (24/08, a raíz de una pregunta de Juan — corregido el mismo día):** al abrir cualquiera de los 4 TTF en un selector de fuente simple (Word, PowerPoint, Canva básico), los pesos no se ven como números — se ven con nombre: `Thin`=100, `ExtraLight`=200, `Light`=300, `Regular`=400, `Medium`=500, `SemiBold`=600, `Bold`=700, `ExtraBold`=800, `Black`=900 (igual en ambas familias, confirmado con `fontTools` leyendo la tabla `fvar`/instancias con nombre). Esto sí quedó documentado en `brandbook.html` (sección 07 — Tipografía, bloque "Nota sobre los archivos de fuente") y en `Guia-Tipografia.pdf`.

Se investigó también si esto afectaba `opsz` (en Bodoni Moda, esas instancias con nombre quedan fijadas a `opsz 11`, no al `opsz 16` usado en el wordmark) — pero al revisar el CSS real, `opsz:16` **solo se aplica a `.wordmark` y `.sidebar-brand`**, es decir, únicamente donde se tipea literalmente el logotipo "WAY". Ningún `.section-title` ni texto general lo usa. Juan pidió (acertadamente) quitar la nota sobre `opsz` porque estaba mal alcanzada — decía "titulares" cuando en realidad es exclusivo del logotipo, y la instrucción que ya queda ("usar siempre los archivos vectoriales de `01-Logo/`, nunca tipear el logo") ya cubre ese único caso real. Se quitó de `brandbook.html` y de `Guia-Tipografia.pdf`, dejando solo la tabla de nombres + esa instrucción.

**Tallas del hang tag y etiqueta tejida con talla (25/08):** Juan pidió 2 correcciones — (1) las tallas van de S a XL, se quita XS del hang tag (`brandbook.html` y `entrega-cliente/`); (2) la etiqueta tejida (`.woven-label`) ahora lleva la talla en un círculo (borde marfil, sin relleno) a la derecha del wordmark — antes solo mostraba el logotipo. Se decidió (con recomendación explícita antes de ejecutar, confirmada por Juan) generar **una variante vectorial por talla (S/M/L/XL) para ambas piezas**, no un solo archivo genérico:
- **Hang tag — frente:** son 4 archivos de producción reales (`hangtag-frente-S/M/L/XL.pdf/.svg`) porque cada prenda física lleva la talla que le corresponde — no tiene sentido un tag "genérico". El dorso sigue siendo un solo archivo (no muestra talla).
- **Etiqueta tejida:** nueva carpeta `entrega-cliente/04-Empaque/07-Etiqueta-Tejida/`, con 4 archivos (`etiqueta-tejida-S/M/L/XL.pdf/.svg`) — pero estos son **referencia de diseño para el proveedor de bordado, no el archivo de producción final** (eso sigue siendo DST/PES, pendiente del proveedor, ya documentado arriba). La etiqueta tejida nunca había sido parte de `entrega-cliente/` antes de este cambio — solo existía como mockup de escala en `brandbook.html`.

**Hang tag sin código de barras — rediseño del frente (02/09):** el frente llevaba una banda de código de barras, una línea de código de producto (`WAY 0000123 L`) y un recuadro punteado "espacio para sticker". Juan pidió eliminar las tres cosas: WAY no usa código de barras, así que la pieza iba a imprenta con un elemento decorativo que no representa nada real. El frente quedó con hoyo → `Talla / Size` + los 4 círculos (en la misma posición vertical que ya tenían, Juan pidió explícitamente **no** recentrar el bloque) → espacio en blanco a propósito → pie. El pie cambió a **`@way_peruvian · wayperuvian.pe`** (se agregó el handle de Instagram y se quitó "Lima, Perú"), que es exactamente la convención de empaque ya usada en la Tarjeta de Agradecimiento — sin número de WhatsApp, por la razón ya documentada. Se regeneraron los 4 PDF + 4 SVG de frente y la `Ficha-Tecnica-HangTag.pdf`; el dorso no se tocó. Se recorrieron 5 variantes de dónde poner el handle antes de cerrar en ésta.

- **Desincronización deliberada con `brandbook.html`:** el alcance de este cambio fue **solo `entrega-cliente/`** (decisión de Juan). `brandbook.html` §"Físico — Escala Real" (regla `.hangtag-barcode`, y el `<div>` correspondiente en el markup del hang tag frente) y `05-Documentos-de-Marca/Brandbook-WAY.pdf` p.31 **siguen mostrando la versión con barras y SKU**. No es un descuido: no "corregir" esto regenerando la entrega desde el brandbook. Si en el futuro se decide alinear el brandbook, hay que quitar ahí `.hangtag-barcode`, `.hangtag-code`, `.hangtag-sticker-space` y actualizar el footer del hang tag frente.
- **La escala real del pipeline de piezas planas es 1 px CSS = 0.75 pt**, no "91 CSS px = 1 pulgada". Verificado midiendo los PDF publicados: `.hangtag` a sus 151 × 340 px nominales de `brandbook.html`, exportado con `page.pdf(width='151px', height='340px', print_background=True, margin=0)`, da 113.25 × 255 pt = 40 × 90 mm, que es justo lo que declara la ficha. Reconstruir el generador así reprodujo el PDF anterior con **0.000 pt** de desviación en los 45 spans — ése es el método para validar cualquier reconstrucción futura: regenerar primero la versión *vieja* y comprobar que da 0, recién entonces aplicar el cambio.
- **No usar `repeating-linear-gradient` (ni ningún relleno con patrón) en piezas de producción.** El código de barras salía del PDF como *tiling pattern* — invisible para `get_images()` y `get_drawings()` — y al derivar el SVG con `get_svg_image()` de PyMuPDF se **rasterizaba**: cada `hangtag-frente-*.svg` cargaba 2 PNG base64 duplicados, contradiciendo el "archivo vectorial real, no referencia" de la propia ficha. Al quitar la banda los SVG bajaron de ~80 KB a ~30 KB y quedaron 100 % vectoriales.
- **La plantilla de las fichas técnicas tampoco persistió.** Se reconstruyó midiendo el PDF publicado con PyMuPDF (A4 595.92 × 842.88 pt; tarjeta `#F7F3EE` de x 51.8 → 545.2 e y 63.0 → 780.0; regla de header `#2A1F18` en y 105.8; título 22 px Bodoni; tabla de 2 columnas con divisoria en x 116.2, celdas `padding: 7px 8px` y `line-height: 1.58`; reglas de fila `#E5DDD2`; bloques de nota y pendiente `#FBF3EC` con barra izquierda terracota de 3 px; pie 7.5 px sobre regla `#E5DDD2`). La reconstrucción quedó a **≤ 2.6 pt (0.92 mm)** del original — el residuo es redondeo sub-pixel de Chromium en 2 filas, no un error de plantilla.

**Pipeline de generación (para regenerar si algo cambia):** igual que el wordmark, este pipeline vivió en el scratchpad de la sesión y no persiste — hay que reconstruirlo desde esta nota. Piezas planas (hang tag, tarjeta, sticker): HTML standalone con el CSS exacto ya aprobado + fuentes embebidas en base64 vía `@font-face` → Playwright local mide el elemento (`getBoundingClientRect`) → `page.pdf()` a ese tamaño exacto en px (91 CSS px = 1 pulgada, ninguna conversión manual de escala) → SVG derivado del PDF ya verificado con `page.get_svg_image()` de PyMuPDF (no se recrea a mano). Nota: un `<svg>` sin `display:block` dentro del body deja un hueco de línea de unos px debajo (comportamiento normal de elemento inline) que puede generar una página extra en blanco al exportar a PDF — pasó una vez con el sticker, se corrigió agregando `display:block` al contenedor. Documentos largos (brandbook + guías): `brandbook.html`/`guia-instagram.html`/`guia-ecommerce.html` ya tienen su propio bloque `@media print` (sidebar oculto, saltos de página por sección) — alcanza con `page.emulate_media('print')` + `page.pdf(format='A4')`, no hace falta CSS adicional.

---

## Archivos del Proyecto

```
way-brandbook/
  brandbook.html               ← entregable principal — Territorio 01, La Firma (v1.1+) — raíz obligatoria (GitHub Pages)
  guia-instagram.html          ← documento operativo separado — calendario, Reels/Stories, comunidad, copy
  guia-ecommerce.html          ← documento operativo separado — diagnóstico y reestructuración de wayperuvian.pe
  estrategia-lanzamiento.html  ← plan de lanzamiento del rebranding (fases, riesgos, transición de assets)
  entrega-cliente/             ← carpeta de entrega para marketing de WAY — ver Notas Técnicas — Carpeta de Entrega
  archivo/                     ← documentos superados o de referencia — no se iteran más (ver nota abajo)
    territorios-way.html         ← presentación histórica de los 3 territorios (ya superada — cliente ya eligió)
    propuesta-identidad.html     ← propuesta histórica de paletas, logos y tipografías (ya superada)
    propuesta-economica-v3.html  ← cotización — versión vigente (v1 y v2 depuradas), sigue siendo la referencia contractual activa aunque viva en archivo/
    AUDITORIA_v1.0.md            ← auditoría independiente de identidad, 13/08, solo lectura — no modifica los documentos auditados
  assets/
    logo/                      ← SVG vectoriales reales (fontTools+Playwright+OpenCV, ver Notas Técnicas)
      way-wordmark-negro.svg          ← logotipo principal, negro sobre transparente — opsz 16
      way-wordmark-marfil.svg         ← versión invertida, marfil sobre transparente — opsz 16
      way-wordmark-embroidery-master.svg ← master engrosado para bordado (peso 800, nunca se ajusta con el resto)
      way-monogram.svg                ← monograma W recto en círculo — avatar/favicon
      favicon.png                     ← 32×32, derivado del monograma
      way-monogram-180.png            ← 180×180, derivado del monograma — generado, aún no enlazado en ningún HTML
      way-wordmark-negro.pdf          ← PDF vectorial, equivalente a AI/EPS — generado con cairosvg, ver Notas Técnicas
      way-wordmark-marfil.pdf         ← ídem, versión invertida
      way-monogram.pdf                ← ídem, monograma
      logo.webp                       ← ⚠️ logo legacy pre-existente, distinto a La Firma — ver nota abajo
    highlights/                ← 10 portadas de highlights de Instagram, PNG reales listos para subir
                                   (círculo marfil + ícono casi-negro) — 9 del sistema permanente ya
                                   mostrado en brandbook.html §10 (mismos paths SVG, exportados como
                                   archivo real) + 1 específico del lanzamiento ("Nueva Imagen",
                                   ver estrategia-lanzamiento.html)
    photos/                    ← generadas (Editorial/Lookbook/Detalle/Promo, Gemini "Nano Banana", fieles
                                   a prendas reales de WAY) + reales del feed actual (@way_peruvian, para
                                   comparativo antes/después) + persona-28-40/45-55/60-65.png (Cliente Ideal)
                                   + empaque-antes-1..4.jpg (fotos reales del empaque físico actual,
                                   provistas por la clienta — identidad anterior, ver sección Empaque)
  CLAUDE.md                    ← este archivo
```

**Nota:** los tres documentos hermanos (`guia-instagram.html`, `guia-ecommerce.html`, `estrategia-lanzamiento.html`) usan `assets/logo/favicon.png` (se actualiza solo, es un archivo compartido) pero tienen su propio CSS de wordmark — ver Notas Técnicas.

### `assets/logo/logo.webp` — confirmado: es el logo actual/vigente de WAY, se documenta como identidad "antes"
Al construir el brandbook se encontró que este archivo ya existía (no estaba vacío como se creía) — es el logo distinto a La Firma (silueta + wordmark en otra tipografía + tagline "Empower yourself") que la marca usa **actualmente**, antes de este rebrand. Confirmado por el cliente. El archivo `logo.webp` en sí no se ha usado en `brandbook.html`, pero esa misma identidad anterior ya aparece documentada ahí de forma indirecta: la sección "Empaque y Materiales Físicos" incluye 4 fotos reales del empaque físico actual (bolsas kraft/papel/plástico, provistas por la clienta el 10/08/2026) que llevan ese mismo logo y tagline.

**Decisión (Juan, 19/08):** se documenta formalmente como identidad "antes" — no se retira. **Implementado (19/08):** insertado en `estrategia-lanzamiento.html`, sección "Transición de Assets" (07 — Fase 4), como comparativo antes/después junto al wordmark nuevo (`.compare-photo--logo-old`/`--logo-new`, variantes nuevas de `.compare-grid` con `aspect-ratio 1/1` + `object-fit: contain`, porque los logos no se recortan bien con el `4:5`/`cover` pensado para fotos de producto). Confirmado visualmente con Juan antes de commitear.

### Hosting
Repo en GitHub: `https://github.com/JuanMosqueraR/way-brandbook` (colaborador: `juanatquanta`). Publicado vía GitHub Pages (Settings → Pages → main → /root). URL pública: `https://juanmosquerar.github.io/way-brandbook/brandbook.html`. **Recordar:** el repo local puede estar adelantado al remoto — confirmar `git status`/`git log origin/main..HEAD` antes de asumir que lo publicado está al día (ver "Estado Actual" arriba).

**Nota:** no usar Claude Artifacts para compartir públicamente este documento — el share público falla consistentemente (probable filtro de moderación por imitar UI de plataformas reales — mockups de Instagram/WhatsApp/TikTok/Shopify). La vista privada de Artifacts sí funciona para revisión interna y para comparativos puntuales que se le mandan a la clienta como link aparte (no como el brandbook completo).

### Claude Design (externo)
- **URL:** https://claude.ai/design
- **Modelo:** Fable 5
- **Proyecto activo:** WAY Brand Identity Territories (ID: `9dbd8d48-5534-4de1-a638-c49f9e2d1217`)
- **Uso:** Generación de propuestas visuales de logo e identidad; documentos de presentación al cliente

---

## Documento de propuesta vs. brandbook final

El documento de Claude Design (mockup HTML/CSS, para elegir dirección) y `brandbook.html` (SVG vectorial real, producción, con zonas de exclusión/usos incorrectos/jerarquía tipográfica/guía de foto/aplicaciones digitales/mockups físicos) son cosas distintas — el primero ya cumplió su función. Pendiente en el segundo: especificaciones de empaque (depende del cliente), archivo de digitalización de bordado (AI/EPS del logo ya resuelto — ver Notas Técnicas).

---

## Pendiente del Cliente

| # | Ítem | Estado |
|---|---|---|
| 1 | Territorio de identidad | ✅ La Firma |
| 2 | Tagline final | ✅ "Con nombre propio" — elegido, actualizado en `brandbook.html` |
| 3 | Historia de origen — ¿por qué "WAY"? | ✅ Respondida por cliente — incorporada en `brandbook.html` |
| 4 | Misión, visión y valores | ✅ Aprobada por la clienta — ver Notas Técnicas / Estado Actual |
| 5 | Ticket promedio | ✅ S/180 |
| 6 | Marcas competidoras / referencia | ✅ Saint Male (@saintmale.cl) |
| 7 | Estilo fotográfico | ✅ Definido — editorial cálido, referencia Saint Male, con regla de autenticidad (Sí/No) en `brandbook.html` |
| 8 | Empaque (bolsas, etiquetas, tissue paper) | ✅ Diseño/dirección validado por la clienta — hang tag y tarjeta de agradecimiento como componentes CSS, bolsa (3 direcciones: kraft, negra, plástica opaca), tissue paper, sticker y caja de envío, con tabla de decisión de bolsa, lineamientos de producción y tabla de aplicación del logo en empaque. Ver Notas Técnicas. **Cotización real de proveedor y fecha de producción quedan fuera del alcance de este proyecto** (decisión de Juan, 19/08) — no son un pendiente abierto, es trabajo que le corresponde a WAY con su proveedor, no al brandbook |
| 9 | Rango de edad cliente ideal | ✅ 28–65+ |
| 10 | Logo vectorial (SVG) | ✅ Generado, más PDF vectorial (equivalente a AI/EPS, sin Illustrator — ver Notas Técnicas). Falta solo el archivo de digitalización de bordado (DST/PES, requiere proveedor) |
| 11 | Cotización formal del proyecto | ✅ Aprobada — S/6,500 (`propuesta-economica-v3.html`), 50% pagado, 50% restante al finalizar el proyecto |
| 12 | Logo legacy (`logo.webp`) | ✅ Se documenta como identidad "antes" (decisión de Juan, 19/08) — no se retira. Falta integrarlo visualmente en `estrategia-lanzamiento.html` (sección Transición de Assets), ver Archivos del Proyecto |
| 13 | Peso/contraste del wordmark | ✅ Resuelto — `opsz 16` final, confirmado por la clienta. Ver Notas Técnicas para el proceso completo y qué hacer si piden más ajuste |
| 14 | Monograma itálica vs. recta | ✅ Resuelto — recta, confirmado por la clienta. Ver Notas Técnicas |
| 15 | Producción por lotes pequeños (dato de negocio) | ✅ Capturado — diferenciador operativo en este archivo y valor de marca "Exclusividad" en `brandbook.html` |
| 16 | Autenticidad fotográfica (piel/rasgos naturales) | ✅ Capturado — regla Sí/No en la sección Fotografía de `brandbook.html` |
| 17 | Fotos reales para la tarjeta "Cliente Ideal" | ✅ Resuelto — 3 fotos generadas con Nano Banana (`persona-28-40.png`, `persona-45-55.png`, `persona-60-65.png`), conectadas en `brandbook.html` |
| 18 | Diferenciación frente a ZARA en el copy del logo | ✅ Resuelto — se agregó texto en `brandbook.html` (sección Logo) aclarando que WAY comparte la convención de wordmark-sin-ícono, no el trazo puntual |

---

## Cotización

✅ **Aprobada y en curso de pago.** Monto final: **S/6,500**. 50% pagado por adelantado, 50% restante al finalizar el proyecto. Documento aprobado: `propuesta-economica-v3.html`.

Contexto histórico (investigación de mercado peruano 2026 que sustentó la propuesta): freelance básico S/500–1,500 · identidad completa desde S/3,500 · branding integral con manual S/6,500–15,000. El brandbook entregado se posicionaba en el tramo alto de "branding integral" por incluir SVG vectorial real, fotografía generada con fidelidad a prendas reales, sistema de aplicaciones digitales completo (IG/WhatsApp/TikTok/Shopify) y mockups físicos funcionales. El rango que se había recomendado internamente era S/8,000–12,000; el monto final negociado y aprobado (S/6,500) quedó por debajo de esa recomendación — dato útil si se cotiza trabajo adicional más adelante (ej. `guia-instagram.html`/`guia-ecommerce.html`, si no estaban incluidas en este monto — confirmar con Juan qué cubre exactamente el S/6,500 acordado).

---

## Próximos Pasos

1. ~~Presentar documento de Claude Design~~ ✅
2. ~~Cliente elige territorio~~ ✅ La Firma
3. ~~Construir `brandbook.html`~~ ✅ — v1.1+, hosteado en GitHub Pages
4. ~~Construir guías operativas~~ ✅ `guia-instagram.html`, `guia-ecommerce.html`
5. ~~Resolver peso/contraste del wordmark y monograma~~ ✅ — ver Notas Técnicas
6. ~~Preparar y aprobar cotización formal~~ ✅ — S/6,500, 50% pagado, `propuesta-economica-v3.html`
7. ~~Hacer `git push` de los commits pendientes~~ ✅ — hecho 21/08, `c6fa4eb..1bdc0f4`, GitHub Pages al día
8. ~~Obtener validación de misión/visión~~ ✅ — aprobada por Lizzie, texto actualizado en `brandbook.html`
9. ~~Iterar `estrategia-lanzamiento.html`~~ ✅ — revisión completa el 21/08: nombres reales (Juan/Nayelli/Lizzie) en todos los responsables, wordmark en PDF vectorial (ver Notas Técnicas), highlights reales generados en `assets/highlights/`, Stories de refuerzo con foto en vez de solo texto, tabla "Quién hace qué", nota de contingencia (si algo no está listo se pospone el Día D completo), captions por opción de Reel. Sigue siendo un documento operativo — puede necesitar ajustes puntuales antes del Día D real (fecha, prenda disponible), pero ya no tiene pendientes estructurales
10. ~~Decidir qué hacer con `logo.webp`~~ ✅ documentado como identidad "antes" e insertado en `estrategia-lanzamiento.html` / Transición de Assets
11. ~~Completar info de empaque~~ ✅ diseño/dirección validado por la clienta — cotización de proveedor y fecha de producción quedan fuera de alcance del proyecto
12. ~~Reorganizar la raíz del repo~~ ✅ — hecho 21/08: `territorios-way.html`, `propuesta-identidad.html`, `propuesta-economica-v3.html` y `AUDITORIA_v1.0.md` se movieron a `archivo/` (con `git mv`, historial preservado). `brandbook.html` y los 3 documentos operativos activos (`guia-instagram.html`, `guia-ecommerce.html`, `estrategia-lanzamiento.html`) se quedaron en la raíz. Única ruta relativa corregida: el favicon de `propuesta-economica-v3.html`. De paso se corrigieron 2 desviaciones que ya existían en este árbol de archivos: `brandbook-v1.0.html` (listado pero ya no existía en el repo, borrado en `f1af94b`) y `AUDITORIA_v1.0.md` (existía desde `5446737` pero nunca se había documentado aquí).
13. ~~Construir carpeta de entrega para marketing (`entrega-cliente/`)~~ ✅ construida 24–25/08, Sticker de Sellado confirmado por Juan sin cambios, pusheada el 25/08 (`69f19fd..4998892`) — ver Notas Técnicas — Carpeta de Entrega.

---

## Reglas del Proyecto

- Todo copy de marca en **español**
- Comentarios de código en **inglés**
- Marcar supuestos con `<!-- ASSUMPTION: ... -->`
- Marcar pendientes con texto visible `[PENDIENTE — Cliente]` en color amber
- `brandbook.html` es autocontenido salvo Google Fonts vía CDN (Bodoni Moda + Archivo) — igual que los documentos de presentación; todo lo demás (logos, fotos) va embebido/local
- Documentos de presentación pueden usar Google Fonts vía CDN
- Claude Design se usa para propuestas visuales; los entregables finales viven en este repo
