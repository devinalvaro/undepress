from .db import Db


class UserdataDb(Db):
    _collection = Db._db.userdata

    def insert(self, **query):
        query['data_id'] = self.get_size() + 1
        super(UserdataDb, self).insert(**query)
