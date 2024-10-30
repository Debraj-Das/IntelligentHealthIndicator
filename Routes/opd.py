from fastapi import APIRouter
from Models.opd import OPD
from DataBase.opd import add_opd, get_opd

router = APIRouter()


@router.post("/opd")
async def create_opd(opd: OPD):
    if not add_opd(opd):
        return {"message": "Failed to create OPD"}
    return {"message": "OPD created successfully"}


@router.get("/opd/{userid}")
async def get_opd(userid: str):
    return get_opd(userid)
