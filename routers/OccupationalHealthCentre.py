from fastapi import APIRouter
from DB.OccupationalHealthCentre import getOHC, addOHC, updateOHC, deleteOHC
from models.OHC import OHC, OHCUpdate

router = APIRouter()


@router.get("/OHC/{id}")
async def occupational(id: int):
    data = await getOHC(id)
    return {"data": data, "message": f"Occupational Health Centre data for the given {id} has been retrieved!"}


@router.post("/OHC")
def create_occupational(newOHC: OHC):
    newdata = addOHC(newOHC)
    return {"data": newdata, "message": "Occupational Health Centre data has been added successfully!"}


@router.put("/OHC/{id}")
def update_occupational(id: int, updatedOHC: OHCUpdate):
    updateddata = updateOHC(updatedOHC)
    return {"data": updateddata, "message": "Occupational Health Centre data has been updated!"}


@router.delete("/OHC/{id}")
def delete_occupational(id: int):
    deleteddata = deleteOHC(id)
    return {"data": deleteddata, "message": "Occupational Health Centre data has been deleted!"}
