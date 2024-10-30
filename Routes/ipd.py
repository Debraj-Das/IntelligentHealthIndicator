from fastapi import APIRouter
from Models.ipd import IPD

router = APIRouter()


@router.post("/ipd")
async def create_ipd(ipd: IPD):
    # store the ipd in the database
    return {"message": "IPD created successfully"}


@router.get("/ipd/{userid}")
async def get_ipd(userid: int):
    # get the ipd from the database
    return {"message": "IPD fetched successfully"}
