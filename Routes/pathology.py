from fastapi import APIRouter
from Models.pathology import Pathology
from DataBase.pathology import add_pathology, get_pathology
from fastapi import File, UploadFile, Form
from typing import Optional
import smtplib
import os
from DataBase.user import get_user

router = APIRouter()


"""
    userid: str
    date: str
    test: str
    result: str = ""
    result_file: str = ""
"""


def send_Notification(userid):
    sender = os.environ.get("SEND_EMAIL")
    password = os.environ.get("SEND_PASSWORD")

    user = get_user(userid)

    if user is None or user["email"] == "None":
        return False

    email = user["email"]

    if sender is None or password is None:
        raise ValueError(
            "SEND_EMAIL and SEND_PASSWORD environment variables must be set")

    message = f"Subject: Abnormal Health Parameter\n\n{user['name']},\n\nYour recent pathology test results show some abnormal health parameters. Please consult a doctor for further diagnosis and treatment."

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, email, message)
        return True

    return False


@router.post("/pathology")
async def create_pathology(
    userid: str = Form(...),
    date: str = Form(...),
    test: str = Form(...),
    result: str = Form(""),
    result_file: Optional[UploadFile] = File(None),
):

    if result_file is None:
        result_file_name = ""
    else:
        result_file_name = f"static/{result_file.filename}"

    pathology = Pathology(userid=userid, date=date, test=test, result=result,
                          result_file=result_file_name)

    if not add_pathology(pathology):
        return {"message": "User not exists"}

    if result_file:
        file_location = f"static/{result_file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(result_file.file.read())

    if len(result) > 4 and result[:4] == "High":
        send_Notification(userid)

    return {"message": "Pathology created successfully"}


@router.get("/pathology/{userid}")
async def get_pathology(userid: str):
    return get_pathology(userid)
