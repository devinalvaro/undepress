from .db import Db


class ChatDb(Db):
    collection = Db._db.chats
