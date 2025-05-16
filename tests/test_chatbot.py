import pytest
from flask.testing import FlaskClient
from chatbot.app import create_app
from chatbot.app import vector_search, vertex


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to your government gateway" in response.data

def test_upload_get(client):
    response = client.get("/upload")
    assert response.status_code == 200

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_chat_post(client: FlaskClient, monkeypatch):
    # Patch vertexai.init to prevent real GCP setup
    monkeypatch.setattr("chatbot.app.vertex.vertexai.init", lambda *args, **kwargs: None)

    # Patch ChatModel.from_pretrained to return a mock model
    class MockChatModel:
        def __call__(self, prompt, **kwargs):
            return type("MockResponse", (), {"text": "Mocked response"})

    monkeypatch.setattr(
        "chatbot.app.vertex.vertexai.preview.language_models.ChatModel.from_pretrained",
        lambda *args, **kwargs: MockChatModel()
    )

    # Patch vector search to return a dummy document
    monkeypatch.setattr("chatbot.app.vector_search.VectorSearch.search", lambda self, q: [
        {"content": "Test doc", "url": "http://example.com"}
    ])

    # Run the actual POST request
    response = client.post("/chat", data={"query": "What is policy X?"})

    assert response.status_code == 200
    assert b"Mocked response" in response.data