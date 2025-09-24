import pandas as pd
from typing import Dict


def normalize_columns(df: pd.DataFrame, mapping: Dict[str, str]) -> pd.DataFrame:
    """
    Renombra columnas según mapping (origen → canónico) y normaliza campos.
    - date: parsea a datetime en formato ISO.
    - amount: convierte a float (quita €, puntos de miles y comas europeas).
    - partner: elimina espacios sobrantes.
    """
    # Renombrar columnas
    df = df.rename(columns=mapping)

    # Normalizar fecha
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce", format="%Y-%m-%d")

    # Normalizar amount
    if "amount" in df.columns:
        df["amount"] = (
            df["amount"]
            .astype(str)
            .str.replace("€", "", regex=False)
            .str.replace(".", "", regex=False)  # puntos de miles
            .str.replace(",", ".", regex=False)  # comas → punto decimal
        )
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    # Limpiar partner
    if "partner" in df.columns:
        df["partner"] = df["partner"].astype(str).str.strip()

    return df


def to_silver(bronze: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega datos desde Bronze a esquema Silver.
    - Agrupa por partner y mes (month).
    - Suma amount en EUR.
    """
    df = bronze.copy()

    if "date" not in df.columns or "amount" not in df.columns or "partner" not in df.columns:
        raise ValueError("Bronze debe contener columnas: date, partner, amount")

    # Crear columna month (timestamp inicio de mes)
    df["month"] = df["date"].dt.to_period("M").dt.to_timestamp()

    silver = (
        df.groupby(["partner", "month"], as_index=False)
        .agg({"amount": "sum"})
    )

    return silver
