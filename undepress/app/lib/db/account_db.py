from .db import Db


class AccountDb(Db):
    collection = Db._db.accounts

    @classmethod
    def insert(cls, **query):
        cls._put_id(query, 'user_id')
        super(AccountDb, cls).insert(**query)

    @classmethod
    def set(cls, query, **update):
        update = cls._filter_none(update)
        super(AccountDb, cls).set(query, **update)
