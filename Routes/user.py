from DataBase.user import add_work_details, user_details
from fastapi import APIRouter
from Models.user import User, WorkDetails
from DataBase.user import add_user, get_user

router = APIRouter()


@router.post("/signup")
async def signup(user: User):
    if not add_user(user):
        return {"message": "User already exists"}
    return {"message": "User created successfully"}


@router.get("/HR/{userid}")
async def Get_user(userid: str):
    result = get_user(userid)

    if result is None:
        return {"message": "User not found"}

    result.pop("_id")

    return result


@router.post("/workDetails")
async def post_workDetails(workDetails: WorkDetails):
    if not add_work_details(workDetails):
        return {"message": "User not Present."}
    return {"message": "WorkDetails has been created successfully."}


@router.get("/workDetails/{userid}")
async def get_workDetails(userid: str):
    result = user_details(userid)
    return result
