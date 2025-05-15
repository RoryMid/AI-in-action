
# 🧠 Government Policy Chatbot + Ingestion System

This project enables users to query policy documents from OECD using a conversational chatbot, powered by Vertex AI and MongoDB vector search.

---

## 🚀 Features

- ✅ PDF ingestion from OECD (Cloud Run, manual trigger)
- ✅ User-uploaded PDFs via chatbot UI (chat-only scope)
- ✅ MongoDB for document and vector storage
- ✅ Google Vertex AI for embeddings and language model
- ✅ Full RAG pipeline with citations and source links
- ✅ Fast Flask frontend with dark mode and animations
- ✅ Deployed via Docker & Terraform on GCP
- ✅ GitHub Actions for CI/CD & test coverage

---

## 🛠️ Local Development

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the chatbot locally:

```bash
export MONGO_URI="your_mongo_uri"
export VERTEX_PROJECT_ID="your_vertex_project_id"
export VERTEX_LOCATION="us-central1"
python chatbot/main.py
```

---

## 🗄️ Secrets Management

All secrets are managed through **Google Secret Manager** and accessed securely by Cloud Run.

### Required GCP Secrets

| Secret Name          | Description                                 |
|----------------------|---------------------------------------------|
| `MONGO_URI`          | MongoDB URI (with username & password)      |
| `VERTEX_PROJECT_ID`  | Your Google Cloud project ID                |
| `VERTEX_LOCATION`    | Vertex AI region (e.g., us-central1)        |

### How to Add Secrets to GCP

```bash
gcloud secrets create MONGO_URI --replication-policy="automatic"
echo -n "your-mongo-uri" | gcloud secrets versions add MONGO_URI --data-file=-

gcloud secrets create VERTEX_PROJECT_ID --replication-policy="automatic"
echo -n "your-project-id" | gcloud secrets versions add VERTEX_PROJECT_ID --data-file=-

gcloud secrets create VERTEX_LOCATION --replication-policy="automatic"
echo -n "your-location" | gcloud secrets versions add VERTEX_LOCATION --data-file=-
```

---

## 🤖 GitHub Actions

### ✅ Tests

Runs on pull requests and pushes to `main`:

- Location: `.github/workflows/test.yml`
- Runs pytest on chatbot + ingestion
- Includes 100% test coverage and monkeypatch mocks

### 🚀 Deployments

Only runs on **pushes to `main`** branch:

- `.github/workflows/deploy-ingestion.yml`
- `.github/workflows/deploy-chatbot.yml`

---

## 🌍 Terraform Deployments

Each module (chatbot + ingestion) includes:

- `terraform/main.tf`: Cloud Run, Secret Manager
- `terraform/variables.tf`: variables per environment
- Deployed via GitHub Actions with Docker

---

## 📁 Project Structure

```bash
.
├── chatbot/
│   ├── main.py
│   ├── app/              # OOP Flask backend
│   ├── static/           # Custom CSS and assets
│   ├── templates/        # Optional, minimal Jinja templates
│   └── tests/            # Unit + integration tests
├── ingestion/
│   ├── main.py
│   ├── oop/
│   ├── terraform/
│   └── tests/
├── .github/workflows/    # CI/CD for deploy + testing
├── requirements.txt
├── Dockerfile
├── .pre-commit-config.yaml
├── README.md
```

---

## 🧪 Testing

Run full test suite:

```bash
pytest --cov=chatbot --cov=ingestion
```

GitHub Actions validates all tests on PRs.

---

## 🧠 About

> “Welcome to your government gateway. If you want to understand how certain policies may affect your society.  
> This project was made by Rory Middleton for a Devpost hackathon.”

![Placeholder image](static/images/home-placeholder.jpg)

---

