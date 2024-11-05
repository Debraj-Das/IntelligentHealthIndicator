from fastapi import APIRouter
from Models.shop import Shop, ShopEnv
from DataBase.shop import add_info, get_info, add_env, shop_details

router = APIRouter()


@router.post("/shop")
async def create_shop(shop: Shop):
    if not add_info(shop):
        return {"message": "Shop already exists"}
    return {"message": "Shop created successfully"}


@router.get("/shop/{shop_id}")
async def get_shop(shop_id: str):
    return get_info(shop_id)


@router.post("/shopenv")
async def post_shop_env(shop_env: ShopEnv):
    if not add_env(shop_env):
        return {"message": "Shop Environment data already exists!"}
    return {"message": "Shop Environment data received successfully!"}


@router.get("/shopenv/{shopid}")
async def get_shop_env(shopid: str):
    return {"data": shop_details(shopid)}
