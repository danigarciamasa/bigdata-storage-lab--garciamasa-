# 📖 Diccionario de Datos (Esquema Canónico)

El esquema canónico define la estructura estándar que adoptarán los datasets una vez transformados a la capa **Silver**.  

## Campos

| Campo   | Tipo        | Descripción                                   | Ejemplo           |
|---------|-------------|-----------------------------------------------|-------------------|
| date    | Date (YYYY-MM-DD) | Fecha del registro en formato ISO 8601       | 2025-09-24        |
| partner | String      | Identificador del socio, cliente o proveedor  | "Partner_A"       |
| amount  | Float (EUR) | Monto de la operación en euros                 | 1520.75           |

---

## Mapeos Origen → Canónico

| Origen (CSV campo) | Canónico (Silver) | Transformación / Regla                           |
|---------------------|-------------------|--------------------------------------------------|
| fecha               | date              | Convertir a formato ISO `YYYY-MM-DD`             |
| day                 | date              | Mapear y normalizar a fecha ISO                  |
| cliente             | partner           | Renombrar a `partner`                            |
| proveedor           | partner           | Renombrar a `partner`                            |
| importe             | amount            | Convertir a float con punto decimal              |
| total_eur           | amount            | Parsear a float, asegurando unidad en EUR        |

> ⚠️ Nota: Todo dataset origen deberá mapear explícitamente sus campos hacia el esquema canónico antes de cargar en Silver.
