from pymongo import MongoClient


class Db:
    __mongo_client = MongoClient('db', 27017)
    _db = __mongo_client.undepress

    @classmethod
    def count(cls, cursor):
        return cursor.count()

    @classmethod
    def find(cls, **query):
        return cls.collection.find(query)

    @classmethod
    def find_one(cls, **query):
        return cls.collection.find_one(query)

    @classmethod
    def insert(cls, **query):
        cls.collection.insert(query)

    @classmethod
    def set(cls, query, **update):
        cls.collection.update(query, {'$set': update}, upsert=True)

    @classmethod
    def unset(cls, query, **update):
        cls.collection.update(query, {'$unset': update})

    @classmethod
    def _put_id(cls, query, key):
        query[key] = cls.count(cls.find()) + 1

    @classmethod
    def _filter_none(cls, query):
        return dict((k, v) for k, v in query.items() if v is not None)
