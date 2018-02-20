from pymongo import MongoClient


class Db:
    __mongo_client = MongoClient('db', 27017)
    _db = __mongo_client.undepress
    _collection = None

    def get_size(self):
        return self.find().count()

    def find(self, **query):
        return self._collection.find(query)

    def find_one(self, **query):
        return self._collection.find_one(query)

    def insert(self, **query):
        self._collection.insert(query)

    def set(self, query, **update):
        self._collection.update(query, {'$set': update})

    def unset(self, query, **update):
        self._collection.update(query, {'$unset': update})
