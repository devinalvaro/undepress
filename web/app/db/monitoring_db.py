from .db import Db


class MonitoringDb(Db):
    Db._collection = Db._db.monitorings
