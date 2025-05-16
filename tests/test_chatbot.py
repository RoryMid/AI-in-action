def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to your government gateway" in response.data

def test_upload_get(client):
    response = client.get("/upload")
    assert response.status_code == 200

def test_chat_post(client, monkeypatch):
    def mock_search(query):
        return [{"content": "Test doc", "url": "http://example.com"}]
    
    def mock_ask(query, docs):
        return "Mock answer", [doc["url"] for doc in docs]

    from chatbot.app import vector_search, vertex
    monkeypatch.setattr("chatbot.app.vector_search.VectorSearch.search", lambda self, q: mock_search(q))
    monkeypatch.setattr(vertex, "ask_vertex_ai", mock_ask)

    response = client.post("/chat", data={"query": "What is policy X?"})
    assert response.status_code == 200
    assert b"Mock answer" in response.data
