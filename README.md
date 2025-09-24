# bigdata-storage-lab--garciamasa-

Aquí tienes un README inicial en formato Markdown para tu laboratorio:

```markdown
# De CSVs heterogéneos a un almacén analítico confiable  
Repositorio: `bigdata-storage-lab-<apellido>`

---

## 🎯 Objetivo
El propósito de este laboratorio es construir un flujo completo de datos que permita transformar **CSVs heterogéneos** en un **almacén analítico confiable**. El pipeline deberá cubrir las siguientes etapas:

1. **Ingesta** → Carga de archivos CSV de diferentes fuentes y estructuras.  
2. **Validación** → Revisión de formatos, tipos y detección de valores faltantes/inconsistentes.  
3. **Normalización** → Estandarización de columnas, formatos de fecha, codificación de categorías y manejo de nulos.  
4. **Bronze / Silver Layers** →  
   - *Bronze*: datos crudos validados.  
   - *Silver*: datos transformados y listos para análisis.  
5. **KPIs** → Cálculo de métricas clave (ejemplo: registros válidos vs. inválidos, cobertura de campos obligatorios, volumen de ingesta semanal).  

---

## 📦 Entregables
- **Repositorio GitHub público** con:  
  - Código del pipeline de ingesta y normalización.  
  - Estructura clara de carpetas (`/src`, `/data`, `/docs`).  
  - README documentando diseño y decisiones técnicas.  
- **Aplicación en Streamlit** para:  
  - Visualizar KPIs de calidad y volumen de datos.  
  - Explorar tablas *silver*.  
  - Mostrar evolución de las métricas.  

---

## ✅ Criterios de Evaluación
1. **Diseño y justificación**: claridad en la arquitectura propuesta y razones de las decisiones.  
2. **Calidad de datos**: correcto tratamiento de nulos, outliers, duplicados y consistencia de tipos.  
3. **Trazabilidad / Data Warehouse**: adecuada separación *bronze/silver*, documentación de linaje y reproducibilidad del pipeline.  
4. **Documentación**: README completo, diagramas simples y explicación del código.  

---

## 🚫 Qué NO subir
- Archivos con **datos sensibles** (personales, financieros, médicos o con propiedad intelectual).  
- Credenciales (tokens, contraseñas, claves de API).  
- Archivos mayores a 50 MB sin justificación.  

---

## ⏱️ Tiempo Estimado por Fase
- Ingesta y validación: **3–4 h**  
- Normalización y diseño *bronze/silver*: **4–5 h**  
- Cálculo de KPIs y pruebas: **2–3 h**  
- Desarrollo app Streamlit: **4–5 h**  
- Documentación y preparación entrega: **2 h**  

**Total estimado**: ~15–19 horas de trabajo.  

---

✍️ **Instrucción**: Personaliza `<apellido>` en el nombre del repo antes de publicar.  
```

¿Quieres que además te genere un **diagrama simple en ASCII** (tipo arquitectura de datos: CSVs → Bronze → Silver → Streamlit) para incluirlo en el README?
