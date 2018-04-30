from .db import Db


class TrainingdataDb(Db):
    collection = Db._db.trainingdata
