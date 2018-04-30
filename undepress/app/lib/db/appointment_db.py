from .db import Db


class AppointmentDb(Db):
    collection = Db._db.appointments
