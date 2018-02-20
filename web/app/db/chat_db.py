from .db import Db


class ChatDb(Db):
    _collection = Db._db.chats
