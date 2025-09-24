def transform_data(df):
    """
    Función de normalización / transformación de datos.
    - Estandariza formatos de fecha.
    - Normaliza nombres de columnas.
    Devuelve DataFrame limpio.
    """
    import pandas as pd

    # Normalizar nombres de columnas
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    # Ejemplo: normalizar fechas si hay columna 'fecha'
    if "fecha" in df.columns:
        df["fecha"] = pd.to_datetime(df["fecha"], errors="coerce")

    return df
