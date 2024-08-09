from DB.HIConnection import DBConnect, DBCommit
from models.OHC import OHC, OHCUpdate

db = DBConnect()


async def getOHC(id: int):
    db.execute(f"SELECT * FROM ohc WHERE userid = {id}")
    return db.fetchall()


async def addOHC(newOHC: OHC):
    db.execute(
        f"INSERT INTO ohc (userid, date, doctor, prescription) VALUES ({newOHC.userid}, '{newOHC.date}', '{newOHC.doctor}', '{newOHC.prescription}') RETURNING *")
    DBCommit()
    return db.fetchone()


async def updateOHC(updatedOHC: OHCUpdate):
    if updatedOHC.id is None:
        return None
    previousDetails = await getOHC(updatedOHC.id)
    if previousDetails is None:
        return None
    i = 0
    for key, value in updatedOHC.model_dump().items():
        if value is None:
            updatedOHC.__setattr__(key, previousDetails[i])
        i += 1
    db.execute(
        f"UPDATE ohc SET userid = {updatedOHC.userid}, date = '{updatedOHC.date}', doctor = '{updatedOHC.doctor}', prescription = '{updatedOHC.prescription}' WHERE userid = {updatedOHC.id} RETURNING *")
    DBCommit()
    return db.fetchone()


async def deleteOHC(id: int):
    db.execute(f"DELETE FROM ohc WHERE userid = {id} RETURNING *")
    DBCommit()
    return db.fetchone()
