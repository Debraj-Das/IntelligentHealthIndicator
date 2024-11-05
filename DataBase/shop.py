import pymongo
import os
from Models.shop import Shop, ShopEnv

client = pymongo.MongoClient(os.getenv("MONGO_URI"))

shop = client['shop']

info = shop['info']
env = shop['env']


def add_info(data: Shop):
    if info.find_one({"shopid": data.shopid}):
        return False
    info.insert_one(data.to_dict())
    return True


def get_info(shopid: str):
    data = info.find_one({"shopid": shopid})
    if data == None:
        return None
    data.pop("_id")
    return {"shop": data}


def add_env(data: ShopEnv):
    if info.find_one({"shopid": data.shopid}) == None:
        return False
    env.insert_one(data.to_dict())
    return True


def shop_details(shopid: str):
    shop_env_data = env.find({"shopid": shopid})
    shop_env = []
    for i in shop_env_data:
        i.pop("_id")
        shop_env.append(i)
    return {"env": shop_env}
