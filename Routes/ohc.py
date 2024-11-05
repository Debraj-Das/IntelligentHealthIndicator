from fastapi import APIRouter
from Models.ohc import OHC
from DataBase.ohc import add_ohc, get_ohc

router = APIRouter()


@router.post("/ohc")
async def ohc(ohc: OHC):
    if not add_ohc(ohc):
        return {"message": "User not exists"}

    return {"message": "OHC created successfully"}


@router.get("/ohc/{userid}")
async def Get_ohc(userid: str):
    ohc = get_ohc(userid)
    data = []
    for i in ohc:
        i.pop("_id")
        data.append(i)

    return {"data": data}
