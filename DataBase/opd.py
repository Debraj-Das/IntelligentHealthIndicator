import pymongo
import os
from Models.opd import OPD

client = pymongo.MongoClient(os.getenv("MONGO_URI"))

opd = client['opd']

opd_collection = opd['opd']


def add_opd(data: OPD):
    opd_collection.insert_one(data.to_dict())
    return True


def get_opd(userid: str):
    return opd_collection.find({"userid": userid})
