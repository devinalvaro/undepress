from .db import Db


class AccountDb(Db):
    _collection = Db._db.accounts

    def insert(self, **query):
        query['user_id'] = self.get_size() + 1
        super(AccountDb, self).insert(**query)
