from .db import Db


class SocmedDb(Db):
    collection = Db._db.socialmedias

    @classmethod
    def set(cls, query, **update):
        update = cls._filter_none(update)
        super(SocmedDb, cls).set(query, **update)
