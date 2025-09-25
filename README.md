# bigdata-storage-lab--garciamasa-

# De CSVs heterogéneos a un almacén analítico confiable  
Repositorio: `bigdata-storage-lab-<apellido>`

---

## 🎯 Objetivo
El propósito de este laboratorio es construir un flujo completo de datos que permita transformar **CSVs heterogéneos** en un **almacén analítico confiable**. El pipeline deberá cubrir las siguientes etapas:

1. **Ingesta** → carga de archivos CSV de diferentes fuentes y estructuras.  
2. **Validación** → revisión de formatos, tipos y detección de valores faltantes/inconsistentes.  
3. **Normalización** → estandarización de columnas, fechas, categorías y nulos.  
4. **Bronze / Silver Layers** →  
   - *Bronze*: datos crudos validados.  
   - *Silver*: datos transformados al esquema canónico.  
5. **KPIs** → métricas clave: % de registros válidos, volumen de ingesta, cobertura de campos obligatorios.

---

## 📦 Entregables
- **Repositorio GitHub público** con:  
  - Código del pipeline de ingesta, validación y normalización.  
  - Estructura clara de carpetas (`/src`, `/data`, `/docs`).  
  - README documentando decisiones técnicas y justificación con las **5V**.  
- **Aplicación en Streamlit** para:  
  - Subida de múltiples CSV heterogéneos.  
  - Validación automática y exploración de datos en Bronze.  
  - Agregación partner×mes en Silver.  
  - Visualización de KPIs y gráfico de evolución.  
  - Descarga de `bronze.csv` y `silver.csv`.

---

## ✅ Criterios de Evaluación
1. **Diseño y justificación**: claridad en la arquitectura propuesta y razones de las decisiones (3 pts).  
2. **Calidad de datos**: correcto tratamiento de nulos, outliers, duplicados y consistencia de tipos (3 pts).  
3. **Trazabilidad / Data Warehouse**: adecuada separación *bronze/silver*, linaje y reproducibilidad (2 pts).  
4. **Documentación**: README completo, diccionario, gobernanza y capturas (2 pts).  

**Total:** 10 puntos.

---

## 🚫 Qué NO subir
- Archivos con **datos sensibles** (personales, financieros, médicos o con propiedad intelectual).  
- Credenciales (tokens, contraseñas, claves de API).  
- Archivos mayores a 50 MB sin justificación.  

---

## ⏱️ Tiempo estimado por fase
- Ingesta y validación: **3–4 h**  
- Normalización y diseño Bronze/Silver: **4–5 h**  
- Cálculo de KPIs y pruebas: **2–3 h**  
- Desarrollo app Streamlit: **4–5 h**  
- Documentación y preparación entrega: **2 h**  

**Total estimado:** 15–19 horas.

---

## 🧪 Checklist de entrega
Ubicado en [`tests/checklist.md`](tests/checklist.md).  
Incluye verificación de:  
- URL Streamlit funcional,  
- `bronze.csv` y `silver.csv` en `/data`,  
- README con decisiones justificadas (5V),  
- Capturas en `/docs/`,  
- Diccionario y gobernanza completos.

---

## 📏 Rúbrica de evaluación (10 puntos)

- **Diseño y justificación** — 3 pts  
- **Calidad de datos** — 3 pts  
- **Trazabilidad y DW** — 2 pts  
- **Documentación** — 2 pts  

Detalle completo en [`docs/rubrica.md`](docs/rubrica.md).

---

## 📖 Documentación asociada
- [`docs/diccionario.md`](docs/diccionario.md) → esquema canónico (`date`, `partner`, `amount`) y mapeos origen.  
- [`docs/gobernanza.md`](docs/gobernanza.md) → linaje, validaciones mínimas, mínimos privilegios, trazabilidad, roles.  

---

## 🧠 Prompts de Reflexión

Responde en este mismo README o en un archivo aparte, en 3–5 líneas máximo cada uno.

1. **V dominante hoy y V dominante si 2× tráfico**  
   - Hoy la **Variedad** es dominante, porque los CSVs llegan con distintos esquemas y la normalización ocupa la mayor parte del esfuerzo.  
   - Si el tráfico se duplicase, la **Velocidad** pasaría a ser el reto principal: procesar en menos tiempo y mantener los SLA de actualización.  
   - La arquitectura debería priorizar pipelines más paralelos o almacenamiento columnar para sostener ese ritmo.

2. **Trade-off elegido (ej. más compresión vs CPU)**  
   - Elegí priorizar **más compresión** en Parquet frente a menos uso de CPU.  
   - Esto reduce significativamente el espacio en disco y el tiempo de lectura en consultas repetidas.  
   - Lo mediré comparando tamaño de archivos y benchmarks de lectura/escritura en CSV vs Parquet.

3. **Por qué “inmutable + linaje” mejora veracidad y qué coste añade**  
   - Inmutabilidad asegura que los datos no se alteran una vez registrados; el linaje permite rastrear su procedencia.  
   - Esto mejora la **veracidad**, porque cada resultado puede verificarse contra su fuente original.  
   - El coste añadido es mayor uso de almacenamiento y complejidad de logs/versionado.

4. **KPI principal y SLA del dashboard (latencia)**  
   - KPI principal: **Total amount mensual por partner**.  
   - SLA: dashboard actualizado cada **24 horas**.  
   - Este KPI habilita decisiones sobre facturación y previsión de ingresos, y esa latencia es suficiente porque el negocio no requiere granularidad en tiempo real.

5. **Riesgo principal del diseño y mitigación técnica concreta**  
   - Riesgo: **inconsistencias de codificación y formatos de origen** que provoquen errores de ingesta.  
   - Mitigación: fallback de encoding (`utf-8` → `latin-1`), validaciones tempranas en Bronze y estandarización de esquema canónico.  
   - De esta forma, los errores se aíslan en capas tempranas y no contaminan Silver ni Gold.

---

✍️ **Instrucción:** Personaliza `<apellido>` en el nombre del repo antes de publicar.

## 🧠 Prompts de Reflexión

Responde a cada punto en 3–5 líneas máximo, justificando con base en tu diseño y datos del laboratorio.

1. V dominante hoy y V dominante si 2× tráfico

Hoy la Variedad es la V dominante, porque recibimos CSVs con esquemas distintos que requieren mappings y normalización.

Si el tráfico se duplicase, la Velocidad se volvería prioritaria: habría que procesar más ficheros en menos tiempo.

Esto exigiría optimizar la ingesta o pasar a formatos columnar (Parquet) para mantener los SLA.

2. Trade-off elegido (ej.: más compresión vs CPU)

Elegí mayor compresión al guardar en Parquet, sacrificando algo de CPU en la escritura.

El beneficio es menor espacio en disco y lecturas más rápidas en análisis repetidos.

Lo mediría comparando tamaños de archivo y tiempos de carga frente a CSV.

3. Por qué “inmutable + linaje” mejora veracidad y qué coste añade

Inmutabilidad evita alterar datos una vez ingeridos y el linaje permite rastrear su origen.

Así se asegura que cualquier análisis puede verificarse contra la fuente.

El coste es más almacenamiento y mantener metadatos de versión, lo que añade complejidad al pipeline.

4. KPI principal y SLA del dashboard (latencia)

KPI: Total amount mensual por partner.

SLA: actualización cada 24 horas, suficiente para decisiones de facturación y control de negocio.

No se requiere tiempo real, pero sí consistencia y puntualidad en la actualización diaria.

5. Riesgo principal del diseño y mitigación técnica concreta

Riesgo: inconsistencias en los nombres de columnas y formatos de origen que rompan la normalización.

Mitigación: usar mapeo dinámico en la app, validaciones tempranas y normalización robusta en Bronze.

Así los errores se detectan antes de llegar a Silver/Gold y no contaminan el análisis.
