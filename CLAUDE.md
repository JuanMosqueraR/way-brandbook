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
- **`estrategia-lanzamiento.html` sigue en iteración activa** — no tratarlo como cerrado. Objetivo explícito del cliente: que la calidad esté a la altura del resto del proyecto, y que quede lo más ejecutable posible para no recargar de trabajo a quienes lo van a llevar a cabo (Lizzie y el/la community manager). También tiene un par de filas en la tabla de Riesgos que hoy están desactualizadas (tagline y acuerdo comercial descritos como si siguieran abiertos) — pendiente de limpieza, no urgente.
- Recomendación de limpieza que quedó **sin decidir**: si vale la pena reorganizar la raíz del repo (ver "Próximos Pasos").

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

## Archivos del Proyecto

```
way-brandbook/
  brandbook.html               ← entregable principal — Territorio 01, La Firma (v1.1+)
  brandbook-v1.0.html          ← respaldo intencional de la versión previa a las mejoras iterativas
  guia-instagram.html          ← documento operativo separado — calendario, Reels/Stories, comunidad, copy
  guia-ecommerce.html          ← documento operativo separado — diagnóstico y reestructuración de wayperuvian.pe
  estrategia-lanzamiento.html  ← plan de lanzamiento del rebranding (fases, riesgos, transición de assets) — ⏳ en iteración activa, ver Estado Actual
  territorios-way.html         ← presentación histórica de los 3 territorios (ya superada — cliente ya eligió)
  propuesta-identidad.html     ← propuesta histórica de paletas, logos y tipografías (ya superada)
  propuesta-economica-v3.html  ← cotización — versión vigente (v1 y v2 depuradas)
  assets/
    logo/                      ← SVG vectoriales reales (fontTools+Playwright+OpenCV, ver Notas Técnicas)
      way-wordmark-negro.svg          ← logotipo principal, negro sobre transparente — opsz 16
      way-wordmark-marfil.svg         ← versión invertida, marfil sobre transparente — opsz 16
      way-wordmark-embroidery-master.svg ← master engrosado para bordado (peso 800, nunca se ajusta con el resto)
      way-monogram.svg                ← monograma W recto en círculo — avatar/favicon
      favicon.png                     ← 32×32, derivado del monograma
      way-monogram-180.png            ← 180×180, derivado del monograma — generado, aún no enlazado en ningún HTML
      logo.webp                       ← ⚠️ logo legacy pre-existente, distinto a La Firma — ver nota abajo
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

El documento de Claude Design (mockup HTML/CSS, para elegir dirección) y `brandbook.html` (SVG vectorial real, producción, con zonas de exclusión/usos incorrectos/jerarquía tipográfica/guía de foto/aplicaciones digitales/mockups físicos) son cosas distintas — el primero ya cumplió su función. Pendiente en el segundo: especificaciones de empaque (depende del cliente), AI/EPS del logo, archivo de digitalización de bordado.

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
| 10 | Logo vectorial (SVG) | ✅ Generado — falta solo AI/EPS (conversión trivial) y archivo de digitalización de bordado (DST/PES, requiere proveedor) |
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
7. ~~Hacer `git push` de los commits pendientes~~ ✅ — hecho 19/08, `4f99d46..a8b4621`, GitHub Pages al día
8. ~~Obtener validación de misión/visión~~ ✅ — aprobada por Lizzie, texto actualizado en `brandbook.html`
9. **Seguir iterando `estrategia-lanzamiento.html`** hasta que esté a la altura del resto del proyecto y sea lo más ejecutable posible para Lizzie/community manager — sigue activo, no tratarlo como cerrado
10. ~~Decidir qué hacer con `logo.webp`~~ ✅ documentado como identidad "antes" e insertado en `estrategia-lanzamiento.html` / Transición de Assets
11. ~~Completar info de empaque~~ ✅ diseño/dirección validado por la clienta — cotización de proveedor y fecha de producción quedan fuera de alcance del proyecto
12. **Decidir** (recomendación abierta, no resuelta) si vale la pena reorganizar la raíz del repo — hoy conviven el documento vivo, un backup intencional, guías operativas y documentos de propuesta ya superados sin ninguna subcarpeta. `brandbook.html` debe quedarse en la raíz sí o sí (GitHub Pages lo sirve desde ahí); cualquier otro archivo que se mueva necesita rutas relativas a `assets/` corregidas.

---

## Reglas del Proyecto

- Todo copy de marca en **español**
- Comentarios de código en **inglés**
- Marcar supuestos con `<!-- ASSUMPTION: ... -->`
- Marcar pendientes con texto visible `[PENDIENTE — Cliente]` en color amber
- `brandbook.html` es autocontenido salvo Google Fonts vía CDN (Bodoni Moda + Archivo) — igual que los documentos de presentación; todo lo demás (logos, fotos) va embebido/local
- Documentos de presentación pueden usar Google Fonts vía CDN
- Claude Design se usa para propuestas visuales; los entregables finales viven en este repo
