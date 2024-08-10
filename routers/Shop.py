from fastapi import APIRouter
from DB.Shop import getShop, createShop, updateShop, deleteShop
from models.Shop import shop, shopUpdate

router = APIRouter()


@router.get("/shop/{shopid}")
async def read_shop(shopid: int):
    data = await getShop(shopid)
    return {"data": data, "message": "Shop has been retrieved!"}


@router.post("/shop")
async def create_shop(newShop: shop):
    data = await createShop(newShop)
    return {"data": data, "message": "Shop has been created!"}


@router.put("/shop/{shopid}")
async def update_shop(shopid: int, updateshop: shopUpdate):
    updateshop.shopid = shopid
    data = await updateShop(updateshop)
    return {"data": data, "message": "Shop has been updated!"}


@router.delete("/shop/{shopid}")
async def delete_shop(shopid: int):
    data = await deleteShop(shopid)
    return {"data": data, "message": "Shop has been deleted!"}
