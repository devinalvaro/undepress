from .db import Db


class AccountDb(Db):
    def __init__(self):
        self.account = self.db.account

    def find(self, email, password=None):
        query = {'email': email}
        if password:
            query['password'] = password

        return self.account.find_one(query)

    def insert(self, email, password):
        query = {'email': email}
        if password:
            query['password'] = password

        self.account.insert_one(query)
