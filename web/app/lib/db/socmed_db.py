from .db import Db


class SocmedDb(Db):
    Db._collection = Db._db.socialmedias

    @staticmethod
    def set(query, **update):
        update = Db._filter_none(update)
        Db.set(query, **update)
