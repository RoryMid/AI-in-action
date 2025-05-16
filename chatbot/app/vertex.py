import os
from vertexai.preview.language_models import ChatModel
import vertexai

vertexai.init(project=os.getenv("VERTEX_PROJECT_ID"), location=os.getenv("VERTEX_LOCATION"))

def ask_vertex_ai(query, docs):
    chat_model = ChatModel.from_pretrained("chat-bison")
    context = "\n".join([doc['content'] for doc in docs])
    chat = chat_model.start_chat()
    response = chat.send_message(f"{context}\n\nAnswer the question: {query}")
    citations = [doc.get('url', '') for doc in docs]
    return response.text, citations
