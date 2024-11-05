import pymongo
import os
from Models.user import User, WorkDetails

client = pymongo.MongoClient(os.getenv("MONGO_URI"))


users = client['user']

user_collection = users['user']
workDetails_collection = users['workDetails']


def add_user(data: User):
    if user_collection.find_one({"userid": data.userid}):
        return False
    user_collection.insert_one(data.to_dict())
    return True


def get_user(userid: str):
    return user_collection.find_one({"userid": userid})


def add_work_details(data: WorkDetails):
    if user_collection.find_one({"userid": data.userid}) == None:
        return False
    workDetails_collection.insert_one(data.to_dict())
    return True


def user_details(userid: str):
    user_work_details = workDetails_collection.find({"userid": userid})
    data = []
    for i in user_work_details:
        i.pop("_id")
        data.append(i)
    return {"data": data}
