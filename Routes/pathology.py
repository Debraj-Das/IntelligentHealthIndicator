from fastapi import APIRouter
from Models.pathology import Pathology
from DataBase.pathology import add_pathology, get_pathology
import smtplib
import os
from DataBase.user import get_user

router = APIRouter()


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
async def create_pathology(pathology: Pathology):

    if not add_pathology(pathology):
        return {"message": "User not exists"}

    result = pathology.result

    userid = get_user(pathology.userid)

    if len(result) > 4 and result[:4] == "High":
        send_Notification(userid)

    return {"message": "Pathology created successfully"}


@router.get("/pathology/{userid}")
async def Get_pathology(userid: str):
    pathology = get_pathology(userid)
    data = []
    for i in pathology:
        i.pop("_id")
        data.append(i)
    return {"data": data}
