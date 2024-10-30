from fastapi import APIRouter
from Models.shopEnv import ShopEnv

router = APIRouter()


@router.post("/shopenv")
async def post_shop_env(shop_env: ShopEnv):
    # shop_env is an instance of ShopEnv
    return {"message": "Shop Environment data received successfully!"}


@router.get("/shopenv/{shopid}")
async def get_shop_env(shopid: int):
    # shopid environment data will be fetched from the database
    result = {}
    return result
