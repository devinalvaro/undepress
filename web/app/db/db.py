from os import environ
from pymongo import MongoClient


class Db:
    __mongo_client = MongoClient(environ['DB_PORT_27017_TCP_ADDR'], 27017)
    _db = __mongo_client.undepress
