from fastapi import APIRouter
from Models.pathology import Pathology

router = APIRouter()


@router.post("/pathology")
async def create_pathology(pathology: Pathology):
    # store the pathology in the database
    return {"message": "Pathology created successfully"}
