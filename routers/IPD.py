from fastapi import APIRouter
from DB.IPD import getIPD, addIPD, updateIPD, deleteIPD
from models.IPD import IPD, IPDUpdate

router = APIRouter()


@router.get("/IPD/{userid}")
async def read_IPD(userid: int):
    data = await getIPD(userid)
    return {"data": data, "message": "IPD has been fetched!"}


@router.post("/IPD")
async def create_IPD(newIPD: IPD):
    data = await addIPD(newIPD)
    return {"data": data, "message": "IPD has been created!"}


@router.put("/IPD/{id}")
async def update_IPD(id: int, updatedIPD: IPDUpdate):
    updatedIPD.id = id
    data = await updateIPD(updatedIPD)
    return {"data": data, "message": "IPD has been updated!"}


@router.delete("/IPD/{id}")
async def delete_IPD(id: int):
    data = await deleteIPD(id)
    return {"data": data, "message": "IPD has been deleted!"}
