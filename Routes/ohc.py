from fastapi import APIRouter
from Models.ohc import OHC
from DataBase.ohc import add_ohc, get_ohc
from fastapi import File, UploadFile, Form
from typing import Optional

router = APIRouter()

"""
    userid: str
    date: str
    doctor: str
    prescription: str = ""
    prescription_file: str = ""
"""


@router.post("/ohc")
async def ohc(
    userid: str = Form(...),
    date: str = Form(...),
    doctor: str = Form(...),
    prescription: str = Form(""),
    prescription_file: Optional[UploadFile] = File(None),
):

    if prescription_file is None:
        prescription_file_name = ""
    else:
        prescription_file_name = f"static/{prescription_file.filename}"

    ohc = OHC(userid=userid, date=date, doctor=doctor, prescription=prescription,
              prescription_file=prescription_file_name)

    if not add_ohc(ohc):
        return {"message": "User not exists"}

    if prescription_file:
        file_location = f"static/{prescription_file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(prescription_file.file.read())

    return {"message": "OHC created successfully"}


@router.get("/ohc/{userid}")
async def get_ohc(userid: str):
    return get_ohc(userid)
