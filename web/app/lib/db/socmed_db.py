from .db import Db


class SocmedDb(Db):
    Db._collection = Db._db.socialmedias
