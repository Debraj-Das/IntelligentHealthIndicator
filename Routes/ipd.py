from fastapi import APIRouter
from Models.ipd import IPD
from DataBase.ipd import add_ipd, get_ipd

router = APIRouter()


@router.post("/ipd")
async def create_ipd(ipd: IPD):
    if not add_ipd(ipd):
        return {"message": "User not exists"}

    return {"message": "IPD created successfully"}


@router.get("/ipd/{userid}")
async def Get_ipd(userid: str):
    ipd = get_ipd(userid)
    data = []
    for i in ipd:
        i.pop("_id")
        data.append(i)
    return {"data": data}
