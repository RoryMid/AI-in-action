def test_mongo_insert(monkeypatch):
    import ingestion.oop.mongo_connector as mongo_connector

    monkeypatch.setattr(mongo_connector, "MongoClient", lambda uri: MockClient())
    mongo = mongo_connector.MongoConnector()
    mongo.insert_document("test.pdf", "content here")

    class MockCollection:
        def insert_one(self, doc):
            assert "filename" in doc
            assert "content" in doc

    class MockClient:
        def __getitem__(self, name):
            return {"documents": MockCollection()}

    monkeypatch.setattr("pymongo.MongoClient", lambda uri: MockClient())
    mongo = MongoConnector()
    mongo.insert_document("test.pdf", "content here")
