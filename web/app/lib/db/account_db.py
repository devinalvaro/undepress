from .db import Db


class AccountDb(Db):
    Db._collection = Db._db.accounts

    @staticmethod
    def insert(**query):
        Db.put_id(query, 'user_id')
        Db.insert(**query)
