from .db import Db


class TokenDb(Db):
    Db._collection = Db._db.tokens
