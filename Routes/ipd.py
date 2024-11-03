from fastapi import APIRouter
from Models.ipd import IPD
from DataBase.ipd import add_ipd, get_ipd
from fastapi import File, UploadFile, Form
from typing import Optional

router = APIRouter()


"""
    userid: str
    admit_no: str
    admission_date: str
    discharge_date: str
    doctor: str
    prescription: str = ""
    prescription_file: str = ""
    status: str = ""
"""


@router.post("/ipd")
async def create_ipd(
    userid: str = Form(...),
    admit_no: str = Form(...),
    admission_date: str = Form(...),
    discharge_date: str = Form(...),
    doctor: str = Form(...),
    prescription: str = Form(""),
    status: str = Form(""),
    prescription_file: Optional[UploadFile] = File(None),
):

    if prescription_file is None:
        prescription_file_name = ""
    else:
        prescription_file_name = f"static/{prescription_file.filename}"

    ipd = IPD(userid=userid, admit_no=admit_no, admission_date=admission_date, discharge_date=discharge_date,
              doctor=doctor, prescription=prescription, prescription_file=prescription_file_name, status=status)

    if not add_ipd(ipd):
        return {"message": "User not exists"}

    if prescription_file:
        file_location = f"static/{prescription_file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(prescription_file.file.read())

    return {"message": "IPD created successfully"}


@router.get("/ipd/{userid}")
async def get_ipd(userid: str):
    return get_ipd(userid)
