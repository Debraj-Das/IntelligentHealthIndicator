from fastapi import APIRouter
from Models.medicine import Medicine
from DataBase.medicine import add_medicine, get_medicine

router = APIRouter()


@router.post("/medicine")
async def create_medicine(medicine: Medicine):
    if not add_medicine(medicine):
        return {"message": "Failed to store medicine."}
    return {"message": "Medicine has been stored successfully."}


@router.get("/medicine/{userid}")
async def get_medicine(userid: str):
    return get_medicine(userid)
