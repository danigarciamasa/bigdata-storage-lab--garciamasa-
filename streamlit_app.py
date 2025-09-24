import io
import pandas as pd
import streamlit as st

from src.ingest import tag_lineage, concat_bronze
from src.validate import basic_checks
from src.transform import normalize_columns, to_silver

st.set_page_config(page_title="Big Data Storage Lab", layout="wide")

st.title("📊 Big Data Storage Lab")
st.markdown(
    "De **CSVs heterogéneos** a un **almacén analítico confiable**: "
    "ingesta → validación → normalización → bronze/silver → KPIs."
)

# --- Sidebar inputs ---
st.sidebar.header("⚙️ Configuración de columnas origen")
col_date = st.sidebar.text_input("Columna de fecha (origen)", value="fecha")
col_partner = st.sidebar.text_input("Columna de partner (origen)", value="cliente")
col_amount = st.sidebar.text_input("Columna de importe (origen)", value="importe")

uploaded_files = st.file_uploader(
    "Sube uno o varios CSVs",
    type=["csv"],
    accept_multiple_files=True,
)

if uploaded_files:
    bronze_frames = []
    st.subheader("📂 Archivos procesados")

    for file in uploaded_files:
        st.markdown(f"**Archivo:** {file.name}")

        # Leer CSV con fallback latin-1
        try:
            df = pd.read_csv(file)
        except UnicodeDecodeError:
            file.seek(0)
            df = pd.read_csv(file, encoding="latin-1")

        # Normalizar columnas al esquema canónico
        mapping = {
            col_date: "date",
            col_partner: "partner",
            col_amount: "amount",
        }
        df = normalize_columns(df, mapping)

        # Añadir linaje
        df = tag_lineage(df, file.name)

        bronze_frames.append(df)

    # --- Bronze unificado ---
    bronze = concat_bronze(bronze_frames)
    st.subheader("🔶 Bronze (unificado)")
    st.dataframe(bronze.head(50), use_container_width=True)

    # Validaciones
    st.subheader("✅ Validaciones")
