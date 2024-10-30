import pymongo
import os
from Models.user import User, WorkDetails

client = pymongo.MongoClient(os.getenv("MONGO_URI"))


users = client['user']

user = users['user']
workDetails = users['workDetails']


def add_user(data: User):
    if user.find_one({"userid": data.userid}):
        return False
    user.insert_one(data.to_dict())
    return True


def get_user(userid: str):
    return user.find_one({"userid": userid})


def add_work_details(data: WorkDetails):
    if user.find_one({"userid": data.userid}) == None:
        return False
    workDetails.insert_one(data.to_dict())
    return True


def user_details(userid: str):
    user_work_details = workDetails.find({"userid": userid})
    return {"workDetails": user_work_details}
