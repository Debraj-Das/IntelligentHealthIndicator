from DB.HIConnection import DBConnect, DBCommit
from models.Medicine import Medicine, MedicineUpdate

db = DBConnect()


async def getMedicinePrescribed(userid: int):
    query = f"SELECT * FROM MedicinePrescribed WHERE userid = {userid}"
    db.execute(query)
    return db.fetchall()


async def addMedicinePrescribed(newMedicine: Medicine):
    query = f"INSERT INTO MedicinePrescribed (userid, medicine, date, doctor, medicine) VALUES ({newMedicine.userid}, '{newMedicine.medicine}', {newMedicine.date}, '{newMedicine.doctor}', '{newMedicine.medicine}') RETURNING *"
    db.execute(query)
    DBCommit()
    return db.fetchone()


async def updateMedicinePrescribed(updatedMedicine: MedicineUpdate):
    if updatedMedicine.id is None:
        return None

    db.execute(
        f"SELECT * FROM MedicinePrescribed WHERE id = {updatedMedicine.id}")
    previousData = db.fetchone()
    if previousData is None:
        return None

    i = 0
    for key, value in updatedMedicine.dict().items():
        if value is None:
            updatedMedicine.__setattr__(key, previousData[i])
        i += 1

    query = f"UPDATE MedicinePrescribed SET userid = {updatedMedicine.userid}, medicine = '{updatedMedicine.medicine}', date = {updatedMedicine.date}, doctor = '{updatedMedicine.doctor}', medicine = '{updatedMedicine.medicine}' WHERE id = {updatedMedicine.id} RETURNING *"

    db.execute(query)
    DBCommit()
    return db.fetchone()


async def deleteMedicinePrescribed(id: int):
    query = f"DELETE FROM MedicinePrescribed WHERE id = {id} RETURNING *"
    db.execute(query)
    DBCommit()
    return db.fetchone()
