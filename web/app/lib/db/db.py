from pymongo import MongoClient


class Db:
    __mongo_client = MongoClient('db', 27017)
    _db = __mongo_client.undepress
    _collection = None

    @staticmethod
    def count(cursor):
        return cursor.count()

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
    def push(query, **update):
        Db._collection.update(query, {'$push': update}, upsert=True)

    @staticmethod
    def set(query, **update):
        Db._collection.update(query, {'$set': update}, upsert=True)

    @staticmethod
    def unset(query, **update):
        Db._collection.update(query, {'$unset': update})

    @staticmethod
    def _put_id(query, key):
        query[key] = Db.count(Db.find()) + 1

    @staticmethod
    def _filter_none(query):
        return dict((k, v) for k, v in query.items() if v is not None)
