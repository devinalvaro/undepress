from pymongo import MongoClient


class Db:
    __mongo_client = MongoClient('db', 27017)
    _db = __mongo_client.undepress
    _collection = None

    @staticmethod
    def put_id(query, key):
        query[key] = Db.get_size() + 1

    @staticmethod
    def get_size():
        return Db.find().count()

    @staticmethod
    def find(**query):
        return Db._collection.find(query)

    @staticmethod
    def find_one(**query):
        return Db._collection.find_one(query)

    @staticmethod
    def insert(**query):
        Db._collection.insert(query)

    @staticmethod
    def set(query, **update):
        Db._collection.update(query, {'$set': update})

    @staticmethod
    def unset(query, **update):
        Db._collection.update(query, {'$unset': update})

    @staticmethod
    def push(query, **update):
        Db._collection.update(query, {'$push': update})
