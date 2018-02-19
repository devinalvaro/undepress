from os import environ
from pymongo import MongoClient


class Db:
    __mongo_client = MongoClient('db', 27017)
    _db = __mongo_client.undepress
