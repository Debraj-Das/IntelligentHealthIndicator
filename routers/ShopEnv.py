from DB.ShopEnv import getShopEnv, addShopEnv, updateShopEnv, deleteShopEnv
from models.ShopEnv import shopEnviroment, shopEnviromentUpdate
from fastapi import APIRouter

router = APIRouter()


@router.get("/shopenv/{shopid}")
async def getShopEnvRoute(shopid: int):
    data = await getShopEnv(shopid)
    return {"data": data, "message": "Data fetched successfully"}


@router.post("/shopenv")
async def addShopEnvRoute(shopEnv: shopEnviroment):
    data = await addShopEnv(shopEnv)
    return {"data": data, "message": "Data added successfully"}


@router.put("/shopenv/{id}")
async def updateShopEnvRoute(id: int, shopEnv: shopEnviromentUpdate):
    shopEnv.id = id
    data = await updateShopEnv(shopEnv)
    return {"data": data, "message": "Data updated successfully"}


@router.delete("/shopenv/{id}")
async def deleteShopEnvRoute(id: int):
    data = await deleteShopEnv(id)
    return {"data": data, "message": "Data deleted successfully"}
