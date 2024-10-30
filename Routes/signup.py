from fastapi import APIRouter
from Models.user import User

router = APIRouter()


@router.post("/signup")
async def signup(user: User):
    print(user)
    return {"message": "User created successfully"}
