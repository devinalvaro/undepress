from .db import Db


class AccountDb(Db):
    __accounts = Db._db.accounts

    def find(self, **query):
        return self.__accounts.find(query)

    def find_one(self, **query):
        return self.__accounts.find_one(query)

    def insert(self, **query):
        query['user_id'] = self.get_size() + 1
        self.__accounts.insert(query)

    def get_size(self):
        return self.find().count()
