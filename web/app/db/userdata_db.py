from .db import Db


class UserdataDb(Db):
    _collection = Db._db.userdata
