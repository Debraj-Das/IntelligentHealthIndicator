import pymongo
import os

client = pymongo.MongoClient(os.getenv("MONGO_URI"))

medicine = client['medicine']


def add_medicine(data):
    medicine.insert_one(data.to_dict())
    return True


def get_medicine(userid):
    return medicine.find_one({"userid": userid})
