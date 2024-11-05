from fastapi import APIRouter
from Models.opd import OPD
from DataBase.opd import add_opd, get_opd

router = APIRouter()


@router.get("/opd/{userid}")
async def Get_opd(userid: str):
    opd = get_opd(userid)
    data = []
    for i in opd:
        i.pop("_id")
        data.append(i)
    return {"data": data}


@router.post("/opd")
async def Add_opd(opd: OPD):

    if not add_opd(opd):
        return {"message": "User not exists"}

    return {"message": "OHC created successfully"}
