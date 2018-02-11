from os import environ
from pymongo import MongoClient


class Db:
    mongo_client = MongoClient(environ['DB_PORT_27017_TCP_ADDR'], 27017)
    db = mongo_client.undepress

    def prepare_query(self, kwargs):
        query = {}
        if kwargs:
            for k, v in kwargs.items():
                query[k] = v

        return query
