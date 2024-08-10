from DB.HIConnection import DBConnect, DBCommit

db = DBConnect()


async def getIPD(userid: int):
    query = f"SELECT * FROM IPD WHERE userid = {userid}"
    db.execute(query)
    return db.fetchall()


async def addIPD(newIPD):
    query = f"INSERT INTO IPD (userid, admit_no, admission_date, discharge_date, doctor, prescription, status) VALUES ({newIPD.userid}, {newIPD.admit_no}, '{newIPD.admission_date}', '{newIPD.discharge_date}', '{newIPD.doctor}', '{newIPD.prescription}', {newIPD.status}) returning *"
    db.execute(query)
    DBCommit()
    return db.fetchall()


async def updateIPD(updatedIPD):
    if updatedIPD.id is None:
        return None

    db.execute(f"SELECT * FROM IPD WHERE id = {updatedIPD.id}")
    previousdata = db.fetchone()
    if previousdata is None:
        return None

    i = 0
    for key, value in updatedIPD.dict().items():
        if value is None:
            updatedIPD.__setattr__(key, previousdata[i])
            i += 1

    query = f"UPDATE IPD SET userid = {updatedIPD.userid}, admit_no = {updatedIPD.admit_no}, admission_date = '{updatedIPD.admission_date}', discharge_date = '{updatedIPD.discharge_date}', doctor = '{updatedIPD.doctor}', prescription = '{updatedIPD.prescription}', status = {updatedIPD.status} WHERE id = {updatedIPD.id} returning *"

    db.execute(query)
    DBCommit()
    return db.fetchone()


async def deleteIPD(id: int):
    query = f"DELETE FROM IPD WHERE id = {id} returning *"
    db.execute(query)
    DBCommit()
    return db.fetchone()
