from fastapi import APIRouter
from DB.HRDetails import getHRDetails, addHRDetails, updateHRDetails, deleteHRDetails
from models.HumanResource import EmployeeDetails, EmployeeDetailsUpdate

router = APIRouter()


@router.get("/HRDetails/{id}")
async def get_hr_details(id: int):
    userDetails = await getHRDetails(id)
    return {"data": userDetails, "message": "HR Details"}


@router.post("/HRDetails")
async def add_hr_details(newHRDetails: EmployeeDetails):
    newHRDetail = await addHRDetails(newHRDetails)
    return {"data": newHRDetail, "message": "HR Details Added"}


@router.put("/HRDetails/{id}")
def update_hr_details(id: int, updatedHRDetails: EmployeeDetailsUpdate):
    update_hr_detail = updateHRDetails(updatedHRDetails)
    return {"data": update_hr_detail, "message": "HR Details Updated"}


@router.delete("/HRDetails/{id}")
def delete_hr_details(id: int):
    deleteHRDetail = deleteHRDetails(id)
    return {"data": deleteHRDetail, "message": "HR Details Deleted"}
