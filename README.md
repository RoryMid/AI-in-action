# Government Gateway Chatbot

A project to ingest planning documents and allow users to interact via a chatbot interface.

## Features

- Upload and parse PDFs
- Chatbot answers questions based on uploaded content
- Vertex AI integration
- MongoDB with vector search (placeholder)

## Setup

1. Install requirements:

pip install -r requirements.txt

2. Set up environment variables using `.env.template`.

3. Run locally:

python chatbot/main.py

4. Ingest documents:

python ingestion/main.py

5. Deploy with Terraform or GitHub Actions.
