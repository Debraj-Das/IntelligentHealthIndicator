from fastapi import APIRouter
from Models.shop import Shop

router = APIRouter()


@router.post("/shop")
async def create_shop(shop: Shop):
    # shop stored in database
    return {"message": "Shop created successfully"}


@router.get("/shop/{shop_id}")
async def get_shop(shop_id: int):
    # get shop from database
    return {"shop_id": shop_id}
