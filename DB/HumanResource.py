from DB.HIConnection import DBConnect, DBCommit
from models.HumanResource import Employee, EmployeeUpdate
from typing import Tuple

db = DBConnect()


async def getEmployeeList():
    db.execute("SELECT * FROM hr_static")
    return db.fetchall()


async def getEmployeeDetails(userid: int):
    db.execute(f"SELECT * FROM hr_static WHERE userid = {userid}")
    return db.fetchone()


async def addEmployee(newEmployee: Employee):
    db.execute(
        f"INSERT INTO hr_static (userid, name, dob, gender, phone, email, joining_date , leaving_date) VALUES ({newEmployee.userid}, '{newEmployee.name}', '{newEmployee.dob}', '{newEmployee.gender}', '{newEmployee.phone}', '{newEmployee.email}' , '{newEmployee.join_date}', '{newEmployee.leaving_date}') RETURNING *")
    DBCommit()
    return db.fetchone()


async def updateEmployee(updatedEmployee: EmployeeUpdate):
    if updatedEmployee.userid is None:
        return None
    previousDetails: Tuple | None = await getEmployeeDetails(updatedEmployee.userid)
    if previousDetails is None:
        return None

    i = 1
    for key, value in updatedEmployee.model_dump().items():
        if value is None:
            updatedEmployee.__setattr__(key, previousDetails[i])
        i += 1

    db.execute(f"UPDATE hr_static SET userid = {updatedEmployee.userid}, name = '{updatedEmployee.name}', dob = '{updatedEmployee.dob}', gender = '{updatedEmployee.gender}', phone = '{updatedEmployee.phone}', email = '{updatedEmployee.email}', joining_date = '{updatedEmployee.join_date}', leaving_date = '{updatedEmployee.leaving_date}' WHERE userid = {updatedEmployee.userid} RETURNING *")
    DBCommit()
    return db.fetchone()


async def deleteEmployee(userid: int):
    db.execute(f"DELETE FROM hr_static WHERE userid = {userid} RETURNING *")
    DBCommit()
    return db.fetchone()
