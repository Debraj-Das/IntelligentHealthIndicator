from fastapi import APIRouter
from pydantic import BaseModel
import smtplib
import os

router = APIRouter()


class Email(BaseModel):
    recipient: str
    subject: str
    message: str


@router.post("/send")
async def send_email(email: Email):
    sender = os.environ.get("SEND_EMAIL")
    password = os.environ.get("SEND_PASSWORD")

    if sender is None or password is None:
        raise ValueError(
            "SEND_EMAIL and SEND_PASSWORD environment variables must be set")

    message = f"Subject: {email.subject}\n\n{email.message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, email.recipient, message)
        return {"message": "Email sent successfully"}
