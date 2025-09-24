# 📏 Rúbrica de Evaluación (10 puntos)

Distribución:
- **Diseño y justificación** — 3 pts
- **Calidad de datos** — 3 pts
- **Trazabilidad y Data Warehouse (DW)** — 2 pts
- **Documentación** — 2 pts

---

## 1) Diseño y justificación (3 pts)
**3 pts (Excelente)**  
- Arquitectura coherente end-to-end (ingesta → validación → normalización → bronze/silver → KPIs).  
- Decisiones técnicas **justificadas explícitamente** en el README, conectadas con las **5V** (Volumen, Velocidad, Variedad, Veracidad, Valor).  
- Mapeos origen→canónico claros y reproducibles.

**2 pts (Bueno)**  
- Flujo mayormente coherente con algunas justificaciones parciales o genéricas.  
- Las 5V se mencionan pero no todas se conectan con decisiones concretas.

**1 pt (Insuficiente)**  
- Falta de coherencia del diseño o ausencia de justificación basada en las 5V.  
- Ambigüedad en el tratamiento de capas o KPIs.

**0 pts (No presentado / falla crítica)**  
- No se puede ejecutar o no hay diseño documentado.

---

## 2) Calidad de datos (3 pts)
**3 pts (Excelente)**  
- `basic_checks` sin errores: columnas canónicas presentes, `amount` numérico y ≥ 0, `date` en datetime.  
- Normalización robusta: fechas ISO, `amount` con limpieza de símbolos/separadores, `partner` depurado.  
- Evidencia de manejo de casos borde (nulos, duplicados, codificaciones).

**2 pts (Bueno)**  
- Validaciones básicas pasan; pequeñas incidencias documentadas y mitigadas.  
- Normalización correcta en la mayoría de campos.

**1 pt (Insuficiente)**  
- Validaciones intermitentes o errores no resueltos.  
- Transformaciones incompletas (fechas o montos inconsistentes).

**0 pts**  
- Datos no validan / inconsistentes sin tratamiento.

---

## 3) Trazabilidad y DW (2 pts)
**2 pts (Excelente)**  
- **Linaje** aplicado (`source_file`, `ingested_at`) y visible en Bronze.  
- Separación clara de capas (*raw/bronze/silver/gold*), con pasos reproducibles.  
- Silver agrega correctamente por **partner × mes**.

**1 pt (Bueno)**  
- Linaje parcial o documentación de linaje mínima.  
- Capas presentes pero con convenciones inconsistentes.

**0 pts**  
- Sin linaje ni separación clara de capas.

---

## 4) Documentación (2 pts)
**2 pts (Excelente)**  
- `docs/diccionario.md` y `docs/gobernanza.md` completos y actualizados.  
- README con instrucciones de despliegue, uso, y capturas en `docs/`.  
- Estructura de repo clara.

**1 pt (Bueno)**  
- Documentación presente con algunos vacíos o desactualizaciones menores.

**0 pts**  
- Documentación insuficiente o ausente.

---

## Nota final
Suma de puntos (0–10). Criterios no acumulables fuera de su máximo por categoría.
