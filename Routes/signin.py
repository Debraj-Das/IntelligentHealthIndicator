from fastapi import APIRouter
from pydantic import BaseModel
from DataBase.user import get_user


class SigninUser(BaseModel):
    userid: str
    password: str


router = APIRouter()


@router.post("/signin")
def signin(user: SigninUser):
    user_data = get_user(user.userid)

    if user_data == None:
        return {"message": "User not found"}

    if user_data["password"] != user.password:
        return {"message": "Invalid password"}

    return {"message": "User signed in successfully", "role": user_data["role"]}
