import pymongo
import os
from Models.ohc import OHC

client = pymongo.MongoClient(os.getenv("MONGO_URI"))

ohc = client['ohc']

ohc_collection = ohc['ohc']


def add_ohc(data: OHC):
    ohc_collection.insert_one(data.to_dict())
    return True


def get_ohc(userid: str):
    return ohc_collection.find({"userid": userid})
