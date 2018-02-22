from .db import Db


class UserdataDb(Db):
    _collection = Db._db.userdata

    def insert(self, **query):
        self.put_id(query, 'data_id')
        super(UserdataDb, self).insert(**query)
