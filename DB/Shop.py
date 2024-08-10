from DB.HIConnection import DBConnect, DBCommit
from models.Shop import shop, shopUpdate

db = DBConnect()


async def getShop(shopid: int):
    query = f"SELECT * FROM shop WHERE shopid = {shopid}"
    db.execute(query)
    return db.fetchall()


async def createShop(shop: shop):
    query = f"INSERT INTO shop (shopid, location) VALUES ({shop.shopid}, '{shop.location}') returning *"
    db.execute(query)
    DBCommit()
    return db.fetchone()


async def updateShop(updateshop: shopUpdate):
    if updateshop.shopid is None:
        return {"message": "Shop ID is required"}

    previouseShop = await getShop(updateshop.shopid)
    if previouseShop is None:
        return {"message": "Shop not found"}

    i = 0
    for key, value in updateshop.model_dump().items():
        if value is None:
            updateShop.__setattr__(key, previouseShop[i])
        i += 1
    query = f"UPDATE shop SET location = '{updateshop.location}' WHERE shopid = {updateshop.shopid} returning *"

    db.execute(query)
    DBCommit()
    return db.fetchone()


async def deleteShop(shopid: int):
    query = f"DELETE FROM shop WHERE shopid = {shopid}"
    db.execute(query)
    DBCommit()
    return {"message": "Shop has been deleted!"}
