from fastapi import APIRouter
from DataBase.analytics import user_infomation_analytics

router = APIRouter()


@router.get("/analytics")
async def analysis(useid: str, starting_date: str, ending_date: str):

    return user_infomation_analytics(useid, starting_date, ending_date)
