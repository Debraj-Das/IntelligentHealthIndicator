from fastapi import APIRouter
from pydantic import BaseModel


class SigninUser(BaseModel):
    userid: str
    password: str


router = APIRouter()


@router.post("/signin")
def signin(user: SigninUser):
    print(user)
    return {"message": "User signed in successfully"}
