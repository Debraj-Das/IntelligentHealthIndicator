from fastapi import APIRouter
from Models.workDetails import WorkDetails

router = APIRouter()


@router.post("/workDetails")
async def post_workDetails(workDetails: WorkDetails):
    return {"message": "WorkDetails has been created successfully."}


@router.get("/workDetails/{userid}")
async def get_workDetails(userid: int):
    result = {}
    return result
