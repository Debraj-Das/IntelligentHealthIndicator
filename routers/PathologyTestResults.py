from fastapi import APIRouter
from DB.PathologyTestResults import getPathologyTestResults, addPathologyTestResults, updatePathologyTestResults, deletePathologyTestResults
from models.Pathology import Pathology, PathologyUpdate

router = APIRouter()


@router.get("/pathology/{userid}")
async def pathology_id(userid: int):
    data = await getPathologyTestResults(userid)
    return {"data": data, "message": "Pathology Test Results has been retrieved!"}


@router.post("/pathology")
async def create_pathology(newPathology: Pathology):
    data = await addPathologyTestResults(newPathology)
    return {"data": data, "message": "Pathology Test Results has been created!"}


@router.put("/pathology/{id}")
async def update_pathology(id: int, newPathology: PathologyUpdate):
    newPathology.id = id
    data = await updatePathologyTestResults(newPathology)
    return {"data": data, "message": "Pathology Test Results has been updated!"}


@router.delete("/pathology/{id}")
async def delete_pathology(id: int):
    data = await deletePathologyTestResults(id)
    return {"data": data, "message": "Pathology Test Results has been deleted!"}
