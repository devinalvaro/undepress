from .db import Db


class ChatDb(Db):
    Db._collection = Db._db.chats
