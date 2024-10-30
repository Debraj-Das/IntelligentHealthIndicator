from fastapi import APIRouter
from Models.medicine import Medicine

router = APIRouter()


@router.post("/medicine")
async def create_medicine(medicine: Medicine):
    # store the medicine in the database
    return {"message": "Medicine has been stored successfully."}


@router.get("/medicine/{userid}")
async def get_medicine(userid: int):
    # fetch the medicine from the database
    return {"message": "Medicine fetched successfully."}
