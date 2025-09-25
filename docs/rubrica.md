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
- Decisiones justificadas explícitamente en el README, conectadas con las **5V**.  

**2 pts (Bueno)**  
- Flujo mayormente coherente con algunas justificaciones parciales o genéricas.  

**1 pt (Insuficiente)**  
- Diseño poco claro o sin relación con las 5V.  

**0 pts**  
- No hay diseño documentado o no se puede ejecutar.

---

## 2) Calidad de datos (3 pts)
**3 pts (Excelente)**  
- `basic_checks` sin errores: columnas canónicas, `amount` numérico y ≥ 0, `date` en datetime.  
- Normalización robusta: fechas ISO, montos estandarizados, partners limpios.  

**2 pts (Bueno)**  
- Validaciones básicas pasan con incidencias menores documentadas.  

**1 pt (Insuficiente)**  
- Validaciones incompletas o errores no resueltos.  

**0 pts**  
- Datos inconsistentes sin tratamiento.

---

## 3) Trazabilidad y DW (2 pts)
**2 pts (Excelente)**  
- Linaje aplicado (`source_file`, `ingested_at`) en Bronze.  
- Separación clara de capas (*raw, bronze, silver, gold*).  

**1 pt (Bueno)**  
- Linaje parcial o documentación mínima.  

**0 pts**  
- Sin linaje ni separación de capas.

---

## 4) Documentación (2 pts)
**2 pts (Excelente)**  
- `docs/diccionario.md` y `docs/gobernanza.md` completos.  
- README con instrucciones, justificación y capturas.  

**1 pt (Bueno)**  
- Documentación presente pero incompleta o desactualizada.  

**0 pts**  
- Documentación insuficiente o ausente.
