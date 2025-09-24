import pandas as pd
from typing import List


def basic_checks(df: pd.DataFrame) -> List[str]:
    """
    Ejecuta validaciones básicas sobre un DataFrame.
    - Verifica presencia de columnas canónicas: date, partner, amount.
    - Comprueba que amount sea numérico y >= 0.
    - Verifica que date sea datetime.
    Devuelve lista de errores encontrados.
    """
    errors: List[str] = []
    required_cols = ["date", "partner", "amount"]

    # Columnas presentes
    for col in required_cols:
        if col not in df.columns:
            errors.append(f"Columna faltante: {col}")

    # Validaciones solo si columnas existen
    if "amount" in df.columns:
        if not pd.api.types.is_numeric_dtype(df["amount"]):
            errors.append("amount no es numérico")
        elif (df["amount"] < 0).any():
            errors.append("amount contiene valores negativos")

    if "date" in df.columns:
        if not pd.api.types.is_datetime64_any_dtype(df["date"]):
            errors.append("date no es datetime")

    return errors
