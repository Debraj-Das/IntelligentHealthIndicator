from fastapi import APIRouter
from Models.ipd import IPD
from DataBase.ipd import add_ipd, get_ipd

router = APIRouter()


@router.post("/ipd")
async def create_ipd(ipd: IPD):
    if not add_ipd(ipd):
        return {"message": "Failed to create IPD"}
    return {"message": "IPD created successfully"}


@router.get("/ipd/{userid}")
async def get_ipd(userid: str):
    return get_ipd(userid)
