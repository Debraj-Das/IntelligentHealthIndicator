from DB.HIConnection import DBConnect, DBCommit
from models.OPD import OPD, OPDUpdate

db = DBConnect()


async def getOPD(userid: int):
    query = f"SELECT * FROM opd WHERE userid = {userid}"
    db.execute(query)
    return db.fetchall()


async def addOPD(opd: OPD):
    query = f"INSERT INTO opd (userid, date, doctor, prescription, status) VALUES ({opd.userid}, '{opd.date}', '{opd.doctor}', '{opd.prescription}', {opd.status}) returning *"
    db.execute(query)
    DBCommit()
    return db.fetchone()


async def updateOPD(opd: OPDUpdate):
    if opd.id == None:
        return None

    db.execute(f"SELECT * FROM opd WHERE id = {opd.id}")
    previousData = db.fetchone()
    if previousData is None:
        return None

    i = 0
    for key, value in opd.model_dump().items():
        if value is None:
            opd.__setattr__(key, previousData[i])
        i += 1

    query = f"UPDATE opd SET userid = {opd.userid}, date = '{opd.date}', doctor = '{opd.doctor}', prescription = '{opd.prescription}', status = {opd.status} WHERE id = {opd.id} returning *"
    db.execute(query)
    DBCommit()
    return db.fetchone()


async def deleteOPD(id: int):
    query = f"DELETE FROM opd WHERE id = {id} returning *"
    db.execute(query)
    DBCommit()
    return db.fetchone()
