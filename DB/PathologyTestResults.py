from DB.HIConnection import DBConnect, DBCommit
from models.Pathology import Pathology, PathologyUpdate

db = DBConnect()

async def getPathologyTestResults(userid: int):
   query = f"SELECT * FROM PathologyTestResults WHERE userid = {userid}"
   db.execute(query)
   return db.fetchall()

async def addPathologyTestResults(newPathology: Pathology):
   query = f"INSERT INTO PathologyTestResults (userid, date, test, result) VALUES ({newPathology.userid}, '{newPathology.date}', '{newPathology.test}', '{newPathology.result}') RETURNING *"
   db.execute(query)
   DBCommit()
   return db.fetchone()

async def updatePathologyTestResults(updatedPathology: PathologyUpdate):
   if updatedPathology.id is None:
      return None

   db.execute(
      f"SELECT * FROM PathologyTestResults WHERE id = {updatedPathology.id}")
   previousData = db.fetchone()
   if previousData is None:
      return None

   i = 0
   for key, value in updatedPathology.dict().items():
      if value is None:
         updatedPathology.__setattr__(key, previousData[i])
      i += 1

   query = f"UPDATE PathologyTestResults SET userid = {updatedPathology.userid}, date = '{updatedPathology.date}', test = '{updatedPathology.test}', result = '{updatedPathology.result}' WHERE id = {updatedPathology.id} RETURNING *"

   db.execute(query)
   DBCommit()
   return db.fetchone()

async def deletePathologyTestResults(id: int):
   query = f"DELETE FROM PathologyTestResults WHERE id = {id} RETURNING *"
   db.execute(query)
   DBCommit()
   return db.fetchone()

async def getMedicinePrescribed(userid: int):
   query = f"SELECT * FROM MedicinePrescribed WHERE userid = {userid}"
   db.execute(query)
   return db.fetchone()