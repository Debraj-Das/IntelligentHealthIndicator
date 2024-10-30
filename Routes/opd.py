from fastapi import APIRouter
from Models.opd import OPD

router = APIRouter()


@router.post("/opd")
async def create_opd(opd: OPD):
    # store the data in the database
    return {"message": "OPD created successfully"}


@router.get("/opd/{userid}")
async def get_opd(userid: int):
    # get the data from the database
    return {"message": "OPD fetched successfully"}
