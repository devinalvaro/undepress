from .db import Db


class UserdataDb(Db):
    Db._collection = Db._db.userdata
