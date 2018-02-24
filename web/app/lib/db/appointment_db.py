from .db import Db


class AppointmentDb(Db):
    Db._collection = Db._db.appointments
