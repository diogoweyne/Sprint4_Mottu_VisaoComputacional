# 🏍️ Sprint 4 – Visão Computacional, MongoDB e Dashboard em Tempo Real | Desafio Mottu

A solução foi desenvolvida para demonstrar a **integração entre Visão Computacional, Banco de Dados e Análise de Dados em tempo real**, permitindo o **monitoramento automatizado de motos no pátio da Mottu**.

Por meio de **detecção com YOLOv8 (Ultralytics)**, **persistência em MongoDB** e um **dashboard interativo em Streamlit**, o sistema realiza o fluxo completo:  
📸 **Captura → 🤖 Processamento → 💾 Armazenamento → 📊 Visualização**

---

## 🧠 Objetivo Geral
> Entregar um protótipo funcional e integrado, evidenciando a comunicação entre a Visão Computacional e o backend, com **persistência real dos dados** em um banco NoSQL (MongoDB) e **visualização dinâmica em tempo real**.

---

## 🧩 Funcionalidades Principais

| Etapa | Descrição | Tecnologias |
|-------|------------|--------------|
| **1️⃣ Captura** | Leitura de vídeo via webcam | OpenCV |
| **2️⃣ Processamento** | Detecção automática de motos com YOLOv8 | Ultralytics YOLO |
| **3️⃣ Persistência** | Salvamento das detecções no **MongoDB** e em arquivo CSV | PyMongo + CSV |
| **4️⃣ Visualização** | Dashboard interativo com métricas e histórico | Streamlit + Pandas |
| **5️⃣ Integração** | Fluxo de dados em tempo real (detecção → banco → dashboard) | Python + MongoDB + Streamlit |

---

## 🧱 Estrutura do Projeto
```
sprint4_mottu/
│
├── README.md
│
├── src/
│   ├── main.py              # Script principal de detecção (YOLO + OpenCV)
│   ├── utils.py             # Funções de persistência (MongoDB + CSV)
│   ├── dashboard.py         # Dashboard em Streamlit (visualização)
│   ├── yolov8n.pt           # Modelo YOLO pré-treinado
│   ├── requirements.txt     # Dependências do projeto
│   └── deteccoes.csv        # Registro local das detecções
│
└── video/
    └── apresentacao_sprint4.mp4
```

---

## ⚙️ Tecnologias Utilizadas

| Categoria | Tecnologias |
|------------|--------------|
| Linguagem | **Python**|
| Visão Computacional | **YOLOv8 (Ultralytics)**, **OpenCV** |
| Banco de Dados | **MongoDB** (via PyMongo) |
| Dashboard | **Streamlit**, **Pandas** |
| Outras Bibliotecas | datetime, os, pymongo, ultralytics, csv |

---

## 🧩 Integração com MongoDB

### 🧰 1️⃣ Instalação
Baixe e instale o **MongoDB Community Server**:  
🔗 [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)

Durante a instalação:
- Mantenha as opções padrão;
- Instale também o **MongoDB Compass** (interface gráfica).

---

### ⚙️ 2️⃣ Conexão utilizada no projeto
O projeto conecta ao banco **local** automaticamente:
```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mottu"]
colecao = db["deteccoes"]
```

Cada detecção é armazenada como documento JSON:
```json
{
  "classe": "motorcycle",
  "data_hora": "2025-11-07T20:52:44.123456"
}
```

---

### 🧭 3️⃣ Visualizando os dados no MongoDB Compass

1. Abra o **MongoDB Compass**  
2. Clique em **Add new connection**  
3. Cole a string:
   ```
   mongodb://localhost:27017
   ```
4. Clique em **Connect**
5. No menu lateral, abra:
   ```
   mottu → deteccoes
   ```
6. Veja os registros das detecções aparecendo em tempo real.

---

## 🔄 Fluxo de Dados Completo

```
[ Câmera / Webcam ]
        ↓
[ main.py - YOLOv8 detecta motos ]
        ↓
[ utils.py - grava no MongoDB + CSV ]
        ↓
[ dashboard.py - lê dados e atualiza interface ]
        ↓
[ Streamlit - Dashboard com métricas e histórico ]
```
---

## 🧾 Execução do Projeto

### 1️⃣ Instalar as dependências
```bash
pip install -r requirements.txt
```

### 2️⃣ Rodar o script de detecção
```bash
python main.py
```

Cada vez que uma moto é detectada:
- A imagem aparece destacada;
- Os dados são gravados no MongoDB e no CSV.

---

### 3️⃣ Rodar o dashboard
Entre na pasta **src**:
```bash
cd src
```
Depois execute:
```bash
python -m streamlit run dashboard.py
```

Acesse o dashboard no navegador:  
👉 [http://localhost:8501](http://localhost:8501)

---

## 👥 Integrantes do Projeto
- **Diogo Weyne - RM558380**
- **Gustavo Tonato Maia - RM555393**
- **João Victor de Souza - RM555290**

---

## 🏆 Conclusão
Este projeto demonstra a aplicação prática e integrada de **Visão Computacional, IoT e Persistência em Banco NoSQL**, simulando o monitoramento automatizado de frotas para o desafio **Mottu**.
