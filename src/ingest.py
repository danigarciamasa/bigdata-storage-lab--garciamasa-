def ingest_data(source_path: str):
    """
    Función de ingesta de datos desde CSV.
    - source_path: ruta del archivo CSV a cargar.
    Devuelve un DataFrame de pandas.
    """
    import pandas as pd
    return pd.read_csv(source_path)
