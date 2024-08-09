from DB.HIConnection import DBConnect, DBCommit
from models.HumanResource import EmployeeDetails, EmployeeDetailsUpdate

db = DBConnect()


async def getHRDetails(id: int):
    db.execute(f"SELECT * FROM hr_dynamic WHERE userid = {id}")
    return db.fetchall()


async def addHRDetails(newHRDetails: EmployeeDetails):
    db.execute(
        f"INSERT INTO hr_dynamic (userid, shopid, shift, grade, joining_shop) VALUES ({newHRDetails.userid}, {newHRDetails.shopid}, '{newHRDetails.shift}', '{newHRDetails.grade}', '{newHRDetails.joining_shop}') RETURNING *")
    DBCommit()
    return db.fetchone()


async def updateHRDetails(updatedHRDetails: EmployeeDetailsUpdate):
    if updatedHRDetails.id is None:
        return None
    previousDetails = await getHRDetails(updatedHRDetails.id)
    if previousDetails is None:
        return None
    i = 0
    for key, value in updatedHRDetails.model_dump().items():
        if value is None:
            updatedHRDetails.__setattr__(key, previousDetails[i])
        i += 1
    db.execute(f"UPDATE hr_dynamic SET userid = {updatedHRDetails.userid}, shopid = {updatedHRDetails.shopid}, shift = '{updatedHRDetails.shift}', grade = '{updatedHRDetails.grade}', joining_shop = '{updatedHRDetails.joining_shop}' WHERE userid = {updatedHRDetails.id} RETURNING *")
    DBCommit()
    return db.fetchone()


async def deleteHRDetails(id: int):
    db.execute(f"DELETE FROM hr_dynamic WHERE userid = {id} RETURNING *")
    DBCommit()
    return db.fetchone()
