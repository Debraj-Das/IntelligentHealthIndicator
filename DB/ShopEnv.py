from DB.HIConnection import DBConnect, DBCommit
from models.ShopEnv import shopEnviroment, shopEnviromentUpdate

db = DBConnect()


async def getShopEnv(shopid: int):
    query = f"SELECT * FROM shop_env WHERE shopid = {shopid}"
    db.execute(query)
    return db.fetchall()


async def addShopEnv(shopEnv: shopEnviroment):
    query = f"INSERT INTO shop_env (shopid, date, temperature, co2_level, humidity) VALUES ({shopEnv.shopid}, '{shopEnv.date}', {shopEnv.temperature}, {shopEnv.co2_level}, {shopEnv.humidity}) returning *"
    db.execute(query)
    DBCommit()
    return db.fetchone()


async def updateShopEnv(shopEnv: shopEnviromentUpdate):
    if shopEnv.id == None:
        return None

    db.execute(f"SELECT * FROM shop_env WHERE id = {shopEnv.id}")
    previousData = db.fetchall()
    if len(previousData) == 0:
        return None

    i = 0
    for key, value in shopEnv.model_dump().items():
        if value is None:
            shopEnv.__setattr__(key, previousData[0][i])
        i += 1

    query = f"UPDATE shop_env SET shopid = {shopEnv.shopid}, date = '{shopEnv.date}', temperature = {shopEnv.temperature}, co2_level = {shopEnv.co2_level}, humidity = {shopEnv.humidity} WHERE id = {shopEnv.id} returning *"
    db.execute(query)
    DBCommit()
    return db.fetchone()


async def deleteShopEnv(id: int):
    query = f"DELETE FROM shop_env WHERE shopid = {id} returning *"
    db.execute(query)
    DBCommit()
    return db.fetchone()
