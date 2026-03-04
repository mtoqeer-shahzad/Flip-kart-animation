# 🛒 Flipkart AI Product Recommender System

![Uploading image.png…]()


---

## 📌 About The Project

**Flipkart AI Product Recommender** is a production-grade AI-powered chatbot that recommends Flipkart products based on user queries. Built using **RAG (Retrieval Augmented Generation)** architecture, the system searches through thousands of product reviews and titles to provide intelligent, context-aware recommendations.

### 💬 Example

```
User  : "Suggest me some gaming headphones under 2000"

Bot   : Based on your query, here are the top recommendations:

        1. 🎧 HyperX Cloud Stinger
           - Great sound quality for gaming
           - Comfortable for long sessions

        2. 🎧 boAt Rockerz 450
           - Excellent bass
           - 15 hours battery life

        3. 🎧 JBL Tune 510BT
           - Clear audio
           - Budget friendly
```

---

## ✨ Features

- 🤖 **AI-Powered Recommendations** — LLaMA 3 via Groq for intelligent responses
- 🔍 **RAG Architecture** — Searches real product reviews for accurate answers
- 💬 **Conversation History** — Remembers previous questions in same session
- ☁️ **Online Vector Database** — AstraDB for scalable vector storage
- 📊 **Monitoring** — Prometheus metrics + Grafana dashboards
- 🐳 **Docker Ready** — Containerized for easy deployment
- ☸️ **Kubernetes Ready** — Production-grade orchestration
- 🌐 **Flask Backend** — Clean REST API with HTML/CSS frontend

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **LLaMA 3.1** via Groq | Large Language Model |
| **HuggingFace Embeddings** | Text to Vector conversion |
| **AstraDB** | Online Vector Database |
| **LangChain** | AI/RAG Framework |
| **Flask** | Backend Web Framework |
| **HTML/CSS** | Frontend UI |
| **Prometheus** | Metrics Collection |
| **Grafana** | Metrics Visualization |
| **Docker** | Containerization |
| **Kubernetes** | Container Orchestration |
| **GCP VM** | Cloud Deployment |
| **GitHub** | Source Code Management |

---

## 🏗️ Project Structure

```
flipkart_product_recommender/
│
├── 📂 flipkart/
│   ├── config.py              # API Keys & Configuration
│   ├── data_convertor.py      # CSV → LangChain Documents
│   ├── data_ingestion.py      # Documents → AstraDB
│   └── rag_chain.py           # RAG Pipeline + Chat History
│
├── 📂 templates/
│   └── index.html             # Frontend UI
│
├── 📂 static/
│   └── style.css              # Styling
│
├── 📂 prometheus/
│   ├── prometheus-deployment.yaml
│   └── prometheus-configmap.yaml
│
├── 📂 data/
│   └── flipkart_review.csv    # Product Reviews Dataset
│
├── 📂 utils/
│   ├── logger.py              # Logging
│   └── custom_exception.py    # Exception Handling
│
├── app.py                     # Flask Application
├── Dockerfile                 # Docker Configuration
├── flask-deployment.yaml      # Kubernetes Deployment
├── requirements.txt           # Python Dependencies
├── setup.py                   # Package Setup
└── .env                       # Environment Variables
```

---

## 🧠 Architecture

```
User Query
    ↓
Flask App (app.py)
    ↓
RAG Chain (rag_chain.py)
    ↓
┌─────────────────────────────┐
│  History Aware Retriever    │
│  (Rewrites question using   │
│   conversation context)     │
└─────────────────────────────┘
    ↓
AstraDB Vector Search
(Top 3 similar products)
    ↓
┌─────────────────────────────┐
│  LLaMA 3 via Groq           │
│  (Generates recommendation  │
│   based on reviews)         │
└─────────────────────────────┘
    ↓
Response to User ✅

Monitoring:
Flask /metrics → Prometheus → Grafana Dashboard 📊
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.10+
- Git

### 1. Clone Repository
```bash
git clone https://github.com/your-username/flipkart-product-recommender.git
cd flipkart-product-recommender
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Linux/Mac
```

### 3. Install Dependencies
```bash
pip install -e .
```

### 4. Setup Environment Variables
Create `.env` file in root directory:
```env
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token
ASTRA_DB_API_ENDPOINT=your_astradb_endpoint
ASTRA_DB_APPLICATION_TOKEN=your_astradb_token
ASTRA_DB_NAMESPACE=default_keyspace
RAG_MODEL=llama-3.1-8b-instant
EMBEDDING_MODEL=BAAI/bge-base-en-v1.5
```

### 5. Get API Keys

| Key | Link | Cost |
|-----|------|------|
| GROQ_API_KEY | [console.groq.com](https://console.groq.com) | Free |
| HF_TOKEN | [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens) | Free |
| AstraDB | [astra.datastax.com](https://astra.datastax.com) | Free |

---

## 🚀 Usage

### Run App Locally
```bash
python app.py
```
Open browser: `http://localhost:5000`

### Ingest Data into AstraDB (First Time Only)
```bash
python -m flipkart.data_ingestion
```

---

## 🐳 Docker Deployment

```bash
# Build image
docker build -t flask-app:latest .

# Run container
docker run -d --name flipkart-app -p 5000:5000 --env-file .env flask-app:latest

# Open browser
http://localhost:5000
```

---

## ☸️ Kubernetes Deployment (GCP VM)

```bash
# Step 1 — Start Minikube
minikube start

# Step 2 — Create Secrets
kubectl create secret generic llmops-secrets \
  --from-literal=GROQ_API_KEY=your_key \
  --from-literal=HF_TOKEN=your_token \
  --from-literal=ASTRA_DB_API_ENDPOINT=your_endpoint \
  --from-literal=ASTRA_DB_APPLICATION_TOKEN=your_token \
  --from-literal=ASTRA_DB_NAMESPACE=default_keyspace

# Step 3 — Deploy App
kubectl apply -f flask-deployment.yaml

# Step 4 — Deploy Prometheus
kubectl apply -f prometheus/prometheus-configmap.yaml
kubectl apply -f prometheus/prometheus-deployment.yaml

# Step 5 — Get URL
minikube service flask-service --url
```

---

## 📊 Monitoring

### Prometheus Metrics
```
http://localhost:5000/metrics

Available Metrics:
- http_requests_total    ← Custom: Total requests
- Python GC metrics      ← Inbuilt: Memory usage
- Process metrics        ← Inbuilt: CPU usage
```

### Grafana Dashboard
```
1. Open Grafana
2. Add Prometheus as data source
3. Create dashboard
4. Query: http_requests_total
```

---

## 🔧 API Reference

| Endpoint | Method | Description |
|---------|--------|-------------|
| `/` | GET | Home page |
| `/get` | POST | Get recommendation |
| `/metrics` | GET | Prometheus metrics |

---

## 👨‍💻 Author

**Muhammad Toqeer Shahzad**
- GitHub: [@mtoqeer-shahzad](https://github.com/mtoqeer-shahzad)

---

## 📄 License

This project is licensed under the MIT License.

---

⭐ **Star this repo if you found it helpful!**
