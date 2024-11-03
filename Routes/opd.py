from fastapi import APIRouter, File, UploadFile, Form
from Models.opd import OPD
from DataBase.opd import add_opd, get_opd
from typing import Optional

router = APIRouter()


@router.get("/opd/{userid}")
async def get_opd(userid: str):
    return get_opd(userid)


"""
    userid: str
    date: str
    doctor: str
    prescription: str = ""
    prescription_file: str = ""
    status: str = ""
"""


@router.post("/opd")
async def create_opd(
    userid: str = Form(...),
    date: str = Form(...),
    doctor: str = Form(...),
    prescription: str = Form(""),
    status: str = Form(""),
    prescription_file: Optional[UploadFile] = File(None),
):

    if prescription_file is None:
        prescription_file_name = ""
    else:
        prescription_file_name = f"static/{prescription_file.filename}"

    opd = OPD(userid=userid, date=date, doctor=doctor, prescription=prescription,
              prescription_file=prescription_file_name, status=status)

    if not add_opd(opd):
        return {"message": "User not exists"}

    if prescription_file:
        file_location = f"static/{prescription_file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(prescription_file.file.read())

    return {"message": "OHC created successfully"}
