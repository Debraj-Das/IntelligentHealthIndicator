from fastapi import APIRouter
from Models.medicine import Medicine
from DataBase.medicine import add_medicine, get_medicine
from fastapi import File, UploadFile, Form
from typing import Optional

router = APIRouter()


"""
    userid: str
    date: str
    doctor: str
    medicine: str = ""
    prescription_file: str = ""
"""


@router.post("/medicine")
async def upload_medicine(
    userid: str = Form(...),
    date: str = Form(...),
    doctor: str = Form(...),
    medicine: str = Form(""),
    prescription_file: Optional[UploadFile] = File(None),
):

    if prescription_file is None:
        prescription_file_name = ""
    else:
        prescription_file_name = f"static/{prescription_file.filename}"

    medicine_data = Medicine(userid=userid, date=date, doctor=doctor,
                             medicine=medicine, prescription_file=prescription_file_name)

    if not add_medicine(medicine_data):
        return {"message": "User not exists"}

    if prescription_file:
        file_location = f"static/{prescription_file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(prescription_file.file.read())

    return {"message": "Medicine created successfully"}


@router.get("/medicine/{userid}")
async def get_medicine(userid: str):
    return get_medicine(userid)
