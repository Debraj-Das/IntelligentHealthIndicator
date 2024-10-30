from fastapi import APIRouter
from Models.ohc import OHC

router = APIRouter()


@router.post("/ohc")
async def ohc(ohc: OHC):
    # store the data in the database
    return {"message": "OHC created successfully"}


@router.get("/ohc/{userid}")
async def get_ohc(userid: int):
    # get the data from the database
    return {"message": "OHC fetched successfully"}
