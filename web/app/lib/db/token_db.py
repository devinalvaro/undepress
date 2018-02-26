from .db import Db


class TokenDb(Db):
    collection = Db._db.tokens
