import pymongo
import os
from Models.ipd import IPD

client = pymongo.MongoClient(os.getenv("MONGO_URI"))

ipd = client['ipd']


def add_ipd(data: IPD):
    ipd.insert_one(data.to_dict())
    return True


def get_ipd(userid: str):
    return ipd.find_one({"userid": userid})
