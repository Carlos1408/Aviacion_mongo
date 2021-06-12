import pymongo
from pymongo import MongoClient
import pprint

class DataBase_mongo:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.db = client.aviacion

    def get_all(self, collection):
        collection = self.db[collection]
        return collection.find()

    def get_spec_document(self, collection, field, value):
        collection = self.db[collection]
        data = collection.find_one({field:value})
        return data

    def get_tags_names(self, collection):
        collection = self.db[collection]
        data = collection.find_one()
        tags = list(data.keys())
        tags.remove('_id')
        return tags

    def get_collection_index(self, collection):
        data = self.get_tags_names(collection)
        return data[0]

db = DataBase_mongo()
# documents = db.get_all('persona')
# documents = db.get_spec_document('persona', 'id', 1)
# documents = db.get_tags_names('persona')
documents = db.get_collection_index('tipo_avion')

if isinstance(documents, (list, tuple)):
    for document in documents:
        pprint.pprint(document)
else:
    pprint.pprint(documents)