from .db import Db


class AccountDb(Db):
    _collection = Db._db.accounts

    def insert(self, **query):
        self.put_id(query, 'user_id')
        super(AccountDb, self).insert(**query)
