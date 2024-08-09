from fastapi import APIRouter
from DB.HumanResource import getEmployeeList, getEmployeeDetails, addEmployee, updateEmployee, deleteEmployee
from models.HumanResource import Employee, EmployeeUpdate

router = APIRouter()


@router.get("/HR")
async def HumanResource():
    AllEmployees = await getEmployeeList()
    print(AllEmployees)
    return {"data": AllEmployees, "message": "All Employees"}


@router.get("/HR/{id}")
async def read_HR(id: int):
    details = await getEmployeeDetails(id)
    return {"data": details, "message": "Employee Details"}


@router.post("/HR")
async def create_HR(Employee: Employee):
    newEmployee = await addEmployee(Employee)
    return {"data": newEmployee, "message": "Employee Added"}


@router.put("/HR/{id}")
async def update_HR(id: int, Employee: EmployeeUpdate):
    Employee.userid = id
    updatedEmployee = await updateEmployee(Employee)
    return {"data": updatedEmployee, "message": "Employee Updated"}


@router.delete("/HR/{id}")
async def delete_HR(id: int):
    deletedEmployee = await deleteEmployee(id)
    return {"data": deletedEmployee, "message": "Employee Deleted"}
