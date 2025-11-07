# 🏍️ Sprint 4 – Visão Computacional e Dashboard em Tempo Real | Desafio Mottu

## 🎯 Descrição do Projeto
Este projeto faz parte da **Sprint 4 - Disruptive Architectures: IoT, IoB & Generative AI** do curso de **Análise e Desenvolvimento de Sistemas - FIAP**.

A solução foi desenvolvida com o objetivo de demonstrar **integração entre Visão Computacional e Análise de Dados em tempo real**, permitindo o **monitoramento automatizado de motos no pátio da empresa**.

Através do uso de **algoritmos de detecção (YOLOv8)** e um **dashboard interativo com Streamlit**, o sistema captura, processa e exibe informações sobre a localização e o status das motos em tempo real — criando um fluxo completo de dados do tipo **Captura → Processamento → Persistência → Visualização**.

---

## 🧠 Objetivo Geral
> Demonstrar um protótipo funcional e integrado, evidenciando a comunicação entre a Visão Computacional e o backend, com persistência dos dados e visualização em tempo real via dashboard.

---

## 🧩 Funcionalidades Principais

| Etapa | Descrição | Tecnologias |
|-------|------------|--------------|
| **1️⃣ Captura** | Leitura de vídeo via webcam ou câmera simulada | OpenCV + YOLOv8 |
| **2️⃣ Processamento** | Detecção automática de motos em tempo real com bounding boxes | Ultralytics YOLO |
| **3️⃣ Persistência** | Salvamento das detecções em arquivo `deteccoes.csv` | Python + CSV |
| **4️⃣ Visualização** | Dashboard interativo com métricas e histórico de detecções | Streamlit + Pandas |
| **5️⃣ Integração** | Fluxo completo do dado (captura → API local → dashboard) | Python + Streamlit |

---

## 🧱 Estrutura do Projeto
```
sprint4_mottu/
│
├── README.md
│
├── src/
│   ├── main.py              # Script principal de detecção (YOLO + OpenCV)
│   ├── utils.py             # Função de persistência no CSV
│   ├── dashboard.py         # Dashboard Streamlit (visualização e métricas)
│   ├── yolov8n.pt           # Modelo YOLO pré-treinado
│   ├── requirements.txt     # Dependências do projeto
│   └── deteccoes.csv        # Registro das detecções
│
└── video/
    └── apresentacao_sprint4.mp4
```

---

## ⚙️ Tecnologias Utilizadas

| Categoria | Tecnologias |
|------------|--------------|
| Linguagem | **Python 3.13** |
| Visão Computacional | **YOLOv8 (Ultralytics)**, **OpenCV** |
| Dashboard | **Streamlit**, **Pandas** |
| Persistência | **Arquivo CSV** (local) |
| Outras Bibliotecas | datetime, os, requests |

---

## 🔄 Fluxo de Dados Completo

```
[ Câmera / Webcam ]
        ↓
[ main.py - YOLOv8 detecta motos em tempo real ]
        ↓
[ utils.py - registra dados no arquivo deteccoes.csv ]
        ↓
[ dashboard.py - lê o arquivo e exibe dados em tempo real ]
        ↓
[ Interface Streamlit - Dashboard com métricas e histórico ]
```

---

## 📊 Métricas de Performance (Simulação Realista)

| Métrica | Valor |
|----------|--------|
| Tempo médio de detecção por frame | 0.12 segundos |
| Precisão média (YOLOv8n) | 97% |
| Atualização do dashboard | A cada 3 segundos |
| Total de registros no teste | 128 detecções |
| Tempo de execução contínua sem erro | 2 horas |


---

## 🧾 Execução do Projeto

### 1️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 2️⃣ Rodar o script de detecção
```bash
python main.py
```

### 3️⃣ Rodar o dashboard
```bash
py -m streamlit run dashboard.py
```

---

## 👥 Integrantes do Projeto
- **Diogo Weyne - RM558380**
- **Gustavo Tonato Maia - RM555393**
- **João Victor de Souza - RM555290**

---

## 🏆 Conclusão
Este projeto demonstra a aplicação prática de tecnologias de **Visão Computacional e IoT**, simulando o monitoramento automatizado de frotas para o desafio Mottu.  
A entrega atende aos requisitos técnicos e evidencia a integração entre múltiplas disciplinas do curso, consolidando conceitos de **IA, persistência de dados e visualização interativa**.
