import pandas as pd
from datetime import datetime, timezone
from typing import List


def tag_lineage(df: pd.DataFrame, source_name: str) -> pd.DataFrame:
    """
    Añade columnas de linaje a un DataFrame:
    - source_file: nombre del archivo origen.
    - ingested_at: timestamp UTC ISO8601.
    """
    df = df.copy()
    df["source_file"] = source_name
    df["ingested_at"] = datetime.now(timezone.utc).isoformat()
    return df


def concat_bronze(frames: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Concatena múltiples DataFrames Bronze y asegura el esquema:
    date, partner, amount, source_file, ingested_at.
    """
    if not frames:
        return pd.DataFrame(columns=["date", "partner", "amount", "source_file", "ingested_at"])

    bronze = pd.concat(frames, ignore_index=True)

    # Reordenar columnas según esquema
    cols = ["date", "partner", "amount", "source_file", "ingested_at"]
    bronze = bronze[cols]

    return bronze
