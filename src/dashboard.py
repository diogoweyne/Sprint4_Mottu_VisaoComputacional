# dashboard.py
import streamlit as st
import pandas as pd
from pymongo import MongoClient

st.set_page_config(page_title="Dashboard Mottu", page_icon="🏍️", layout="wide")
st.title("🏍️ Dashboard de Detecções - Mottu (MongoDB)")

try:
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mottu"]
    colecao = db["deteccoes"]
    dados = list(colecao.find({}, {"_id": 0}))  # não mostrar o campo _id

    df = pd.DataFrame(dados)

    if not df.empty:
        col1, col2, col3 = st.columns(3)
        col1.metric("📈 Total de Detecções", len(df))
        col2.metric("🕒 Última Detecção", df["data_hora"].iloc[-1])
        col3.metric("📍 Última Classe", df["classe"].iloc[-1])

        st.dataframe(df.sort_values(by="data_hora", ascending=False), width='stretch')
    else:
        st.warning("Nenhuma detecção registrada ainda.")

except Exception as e:
    st.error(f"⚠️ Erro ao conectar ao MongoDB: {e}")
