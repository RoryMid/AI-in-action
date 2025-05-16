import os
from pymongo import MongoClient

class MongoHandler:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI'))
        self.db = self.client["chatbot"]
        self.collection = self.db["documents"]

    def get_relevant_documents(self, query):
        # Simplified placeholder for vector search
        return list(self.collection.find().limit(3))

    def get_all_ingested(self):
        return list(self.collection.find({}, {"filename": 1, "url": 1, "_id": 0}))

    def insert_uploaded_pdf(self, path):
        with open(path, 'rb') as f:
            content = f.read().decode('latin1')
        self.collection.insert_one({
            "content": content,
            "filename": os.path.basename(path),
            "source": "upload"
        })
