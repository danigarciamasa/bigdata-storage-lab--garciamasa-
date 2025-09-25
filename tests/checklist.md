# ✅ Checklist de Entrega

Marque cada casilla al completar el punto. Incluya evidencias (enlaces o capturas) donde corresponda.

## 1) Despliegue
- [ ] **URL Streamlit funcional** (pública en Streamlit Community Cloud)  
      Link: https://fadfrnxwlxppcylkr8uqho.streamlit.app/

## 2) Artefactos de datos
- [ ] **bronze.csv** subido a `data/bronze/`  
      Ruta/commit: data/bronze/bronze.csv
- [ ] **silver.csv** subido a `data/silver/`  
      Ruta/commit: data/silver/silver.csv

## 3) Documentación principal
- [ ] **README** con decisiones justificadas, conectando las **5V del Big Data** con las elecciones del diseño  
      (Ingesta, Validación, Normalización, Bronze/Silver, KPIs)  
      Link al README: _____________________________________________________
- [ ] **Capturas** de la app (pantallas clave) guardadas en `docs/`  
      (Subida de CSV, Validaciones, Bronze, Silver, KPIs/Gráfico)  
      Rutas/commit: _______________________________________________________

## 4) Diccionario y gobernanza
- [ ] `docs/diccionario.md` **completo y actualizado** con el esquema canónico  
- [ ] `docs/gobernanza.md` **completo y actualizado** (linaje, validaciones mínimas, mínimos privilegios, trazabilidad, roles)

---

## Verificaciones rápidas
- [ ] La app permite subir **múltiples CSV** y mapear columnas de origen en el sidebar
- [ ] `basic_checks` no reporta errores en los datos finales
- [ ] `to_silver` agrega correctamente por **partner × mes**
- [ ] El **bar chart** se renderiza y muestra la suma mensual de `amount`
- [ ] Los botones de **descarga** de `bronze.csv` y `silver.csv` funcionan
