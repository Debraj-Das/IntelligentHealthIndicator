from fastapi import APIRouter
from DB.MedicinePrescribed import getMedicinePrescribed, addMedicinePrescribed, updateMedicinePrescribed, deleteMedicinePrescribed
from models.Medicine import Medicine, MedicineUpdate

router = APIRouter()


@router.get("/medicine/{userid}")
async def medicine_id(userid: int):
    data = await getMedicinePrescribed(userid)
    return {"data": data, "message": "Medicine Prescribed has been retrieved!"}


@router.post("/medicine")
async def create_medicine(newMedicine: Medicine):
    data = await addMedicinePrescribed(newMedicine)
    return {"message": "Medicine Prescribed has been created!"}


@router.put("/medicine/{id}")
async def update_medicine(id: int, updatedMedicine: MedicineUpdate):
    updatedMedicine.id = id
    data = await updateMedicinePrescribed(updatedMedicine)
    return {"data": data, "message": "Medicine Prescribed has been updated!"}


@router.delete("/medicine/{id}")
async def delete_medicine(id: int):
    data = await deleteMedicinePrescribed(id)
    return {"data": data, "message": "Medicine Prescribed has been deleted!"}
