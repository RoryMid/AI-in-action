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
    # Mock vector search
    monkeypatch.setattr("chatbot.app.vector_search.VectorSearch.search", lambda self, q: [
        {"content": "Test doc", "url": "http://example.com"}
    ])

    monkeypatch.setattr(vertex, "ask_vertex_ai", mock_ask)

    # Mock ask_vertex_ai directly to avoid triggering VertexAI auth
    def mock_ask(query, docs):
        return "Mocked response", ["http://example.com"]

    # Now trigger the route
    response = client.post("/chat", data={"query": "What is policy X?"})
    assert response.status_code == 200
    assert b"Mocked response" in response.data
