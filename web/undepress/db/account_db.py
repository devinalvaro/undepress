from .db import Db


class AccountDb(Db):
    def __init__(self):
        self.account = self.db.account

    def find(self, **kwargs):
        query = self.prepare_query(kwargs)
        return self.account.find(query)

    def find_one(self, **kwargs):
        query = self.prepare_query(kwargs)
        return self.account.find_one(query)

    def size(self, **kwargs):
        return self.find().count()

    def insert(self, **kwargs):
        query = self.prepare_query(kwargs)
        query['user_id'] = self.size() + 1

        self.account.insert_one(query)
