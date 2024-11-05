import pymongo
import os

client = pymongo.MongoClient(os.getenv("MONGO_URI"))

medicine = client['medicine']

medicine_collection = medicine['medicine']


def add_medicine(data):
    medicine_collection.insert_one(data.to_dict())
    return True


def get_medicine(userid):
    return medicine_collection.find({"userid": userid})
