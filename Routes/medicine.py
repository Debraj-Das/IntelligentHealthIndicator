from fastapi import APIRouter
from Models.medicine import Medicine
from DataBase.medicine import add_medicine, get_medicine

router = APIRouter()


@router.post("/medicine")
async def upload_medicine(medicine: Medicine):

    if not add_medicine(medicine):
        return {"message": "User not exists"}

    return {"message": "Medicine created successfully"}


@router.get("/medicine/{userid}")
async def Get_medicine(userid: str):
    medicine = get_medicine(userid)
    data = []
    for i in medicine:
        i.pop("_id")
        data.append(i)
    return {"data": data}
