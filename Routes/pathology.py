from fastapi import APIRouter
from Models.pathology import Pathology
from DataBase.pathology import add_pathology, get_pathology

router = APIRouter()


@router.post("/pathology")
async def create_pathology(pathology: Pathology):
    if not add_pathology(pathology):
        return {"message": "Failed to create Pathology"}
    return {"message": "Pathology created successfully"}


@router.get("/pathology/{userid}")
async def get_pathology(userid: str):
    return get_pathology(userid)
