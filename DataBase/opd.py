import pymongo
import os
from Models.opd import OPD

client = pymongo.MongoClient(os.getenv("MONGO_URI"))

opd = client['opd']


def add_opd(data: OPD):
    opd.insert_one(data.to_dict())
    return True


def get_opd(userid: str):
    return opd.find_one({"userid": userid})
