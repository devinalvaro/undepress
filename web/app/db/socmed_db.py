from .db import Db


class SocmedDb(Db):
    _collection = Db._db.socialmedias
