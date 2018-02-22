from .db import Db


class UserdataDb(Db):
    Db._collection = Db._db.userdata

    @staticmethod
    def insert(**query):
        Db.put_id(query, 'data_id')
        Db.insert(**query)
