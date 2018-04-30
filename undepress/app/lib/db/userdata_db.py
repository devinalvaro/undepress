from .db import Db


class UserdataDb(Db):
    collection = Db._db.userdata
