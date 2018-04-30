from .db import Db


class MonitoringDb(Db):
    collection = Db._db.monitorings
