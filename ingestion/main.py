from ingestion.oop.pdf_ingestor import PDFIngestor
from ingestion.oop.mongo_connector import MongoConnector

def main():
    connector = MongoConnector()
    ingestor = PDFIngestor(connector)
    ingestor.ingest_directory("data")

if __name__ == "__main__":
    main()
