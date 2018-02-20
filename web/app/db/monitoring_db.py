from .db import Db


class MonitoringDb(Db):
    _collection = Db._db.monitorings
