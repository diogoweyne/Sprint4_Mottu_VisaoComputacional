# utils.py
from pymongo import MongoClient
import csv
import os

def salvar_deteccao(dados):
    """
    Salva a detecção no CSV e também no MongoDB.
    """
    # --- Salvar no CSV (backup local) ---
    file = "deteccoes.csv"
    existe = os.path.exists(file)
    with open(file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["classe", "data_hora"])
        if not existe:
            writer.writeheader()
        writer.writerow(dados)
    print(f"💾 Detecção salva no CSV: {dados}")

    # --- Salvar no MongoDB ---
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["mottu"]               # nome do banco
        colecao = db["deteccoes"]          # nome da coleção
        colecao.insert_one(dados)
        print("✅ Detecção salva no MongoDB com sucesso.")
    except Exception as e:
        print(f"⚠️ Erro ao salvar no MongoDB: {e}")
