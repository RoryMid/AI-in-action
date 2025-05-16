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
    flask_app = create_app()
    flask_app.testing = True
    return flask_app.test_client()

def test_chat_post(monkeypatch, client):
    class MockResponse:
        def __init__(self, text):
            self.text = text

    class MockChatSession:
        def send_message(self, prompt):
            return MockResponse("Mocked answer")

    class MockChatModel:
        def start_chat(self, **kwargs):
            return MockChatSession()

    monkeypatch.setattr("chatbot.vertex.ChatModel", lambda **kwargs: MockChatModel())

    response = client.post("/chat", json={"prompt": "Test prompt"})
    assert response.status_code == 200
    assert "Mocked answer" in response.get_json()["response"]