import os

class PDFIngestor:
    def __init__(self, mongo_connector):
        self.mongo_connector = mongo_connector

    def ingest_directory(self, dir_path):
        for filename in os.listdir(dir_path):
            if filename.endswith(".pdf"):
                with open(os.path.join(dir_path, filename), "rb") as f:
                    content = f.read().decode('latin1')
                    self.mongo_connector.insert_document(filename, content)
