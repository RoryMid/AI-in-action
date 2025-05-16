from pymongo import MongoClient
import os

class MongoConnector:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGO_URI"))
        self.db = self.client["chatbot"]
        self.collection = self.db["documents"]

    def insert_document(self, filename, content):
        self.collection.insert_one({
            "filename": filename,
            "content": content,
            "source": "batch-ingest"
        })
