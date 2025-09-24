def validate_data(df):
    """
    Función de validación de datos.
    - Verifica tipos, nulos y duplicados.
    Devuelve un diccionario con resultados de validación.
    """
    report = {
        "n_rows": len(df),
        "n_nulls": df.isnull().sum().to_dict(),
        "n_duplicates": df.duplicated().sum(),
        "dtypes": df.dtypes.astype(str).to_dict()
    }
    return report
