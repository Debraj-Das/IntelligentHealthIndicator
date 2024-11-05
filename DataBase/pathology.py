import pymongo
import os

client = pymongo.MongoClient(os.getenv("MONGO_URI"))

pathology = client['pathology']

pathology_collection = pathology['pathology']


def add_pathology(data):
    pathology_collection.insert_one(data.to_dict())
    return True


def get_pathology(userid):
    return pathology_collection.find({"userid": userid})
