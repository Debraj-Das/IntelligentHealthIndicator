from fastapi import APIRouter
from DB.OPD import getOPD, addOPD, updateOPD, deleteOPD
from models.OPD import OPD, OPDUpdate

router = APIRouter()


@router.get("/OPD/{userid}")
async def read_OPD(userid: int):
    data = await getOPD(userid)
    return {"data": data, "message": "Data fetched successfully"}


@router.post("/OPD")
async def create_OPD(newOPD: OPD):
    data = await addOPD(newOPD)
    return {"data": data, "message": "OPD has been created!"}


@router.put("/OPD/{id}")
async def update_OPD(id: int, updatedOPD: OPDUpdate):
    updatedOPD.id = id
    data = await updateOPD(updatedOPD)
    return {"data": data, "message": "OPD has been updated!"}


@router.delete("/OPD/{id}")
async def delete_OPD(id: int):
    data = await deleteOPD(id)
    return {"data": data, "message": "OPD has been deleted!"}
