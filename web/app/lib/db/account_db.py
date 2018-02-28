from .db import Db


class AccountDb(Db):
    collection = Db._db.accounts

    @classmethod
    def find(cls, **query):
        exclude = dict(password=0)
        return cls.collection.find(query, exclude)

    @classmethod
    def find_one(cls, **query):
        exclude = dict(password=0)
        return cls.collection.find_one(query, exclude)

    @classmethod
    def insert(cls, **query):
        cls._put_id(query, 'user_id')
        super(AccountDb, cls).insert(**query)

    @classmethod
    def set(cls, query, **update):
        update = cls._filter_none(update)
        super(AccountDb, cls).set(query, **update)
