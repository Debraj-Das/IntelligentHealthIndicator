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
    return info.find_one({"shopid": shopid})


def add_env(data: ShopEnv):
    if info.find_one({"shopid": data.shopid}) == None:
        return False
    env.insert_one(data.to_dict())
    return True


def shop_details(shopid: str):
    shop = get_info(shopid)
    if (shop == None):
        return None
    shop_env = env.find({"shopid": shopid})
    return {"shop": shop, "env": shop_env}
