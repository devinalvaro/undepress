from .db import Db


class TrainingdataDb(Db):
    Db._collection = Db._db.trainingdata
