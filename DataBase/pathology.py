import pymongo
import os

client = pymongo.MongoClient(os.getenv("MONGO_URI"))

pathology = client['pathology']


def add_pathology(data):
    pathology.insert_one(data.to_dict())
    return True


def get_pathology(userid):
    return pathology.find_one({"userid": userid})
