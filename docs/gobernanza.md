# 🛡️ Gobernanza de Datos

Este documento define las políticas y buenas prácticas de gestión de datos para el laboratorio.

---

## 1. Origen y Linaje
- **Origen**: Archivos CSV heterogéneos cargados en la capa *raw*.  
- **Linaje**:  
  - *Raw* → datos tal cual del proveedor.  
  - *Bronze* → datos validados y limpiados mínimamente.  
  - *Silver* → datos normalizados al esquema canónico.  
  - *Gold* → datasets listos para analítica y KPIs.  

Cada transformación debe documentarse con:
- Script responsable (`ingest.py`, `validate.py`, `transform.py`).  
- Fecha y versión de la carga.  

---

## 2. Validaciones mínimas
- Comprobar integridad de fechas (`date` en formato ISO).  
- Asegurar que `partner` no esté vacío.  
- Validar que `amount` sea numérico y en EUR.  
- Reportar número de duplicados y nulos.  

---

## 3. Política de mínimos privilegios
- Acceso a *raw*: solo equipo de ingeniería de datos.  
- Acceso a *silver*: equipo de ingeniería + analistas.  
- Acceso a *gold*: todos los consumidores autorizados.  
- Ningún usuario debe tener más permisos de los estrictamente necesarios.  

---

## 4. Trazabilidad
- Mantener logs de ejecución y validación.  
- Generar reportes automáticos de calidad (KPIs).  
- Versionar scripts y documentación en GitHub.  
- Registrar cambios en el diccionario de datos.  

---

## 5. Roles
- **Data Engineer**: diseño y mantenimiento del pipeline, ingesta y transformación.  
- **Data Steward**: seguimiento de calidad y actualización de diccionario.  
- **Data Analyst**: análisis sobre capas *silver* y *gold*.  
- **Product Owner**: garante de la utilidad del dato y alineación con negocio.  
