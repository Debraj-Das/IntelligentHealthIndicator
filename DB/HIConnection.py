import psycopg2 as pg
import os
from dotenv import load_dotenv

load_dotenv()

dbConnection = pg.connect(
    host=os.getenv("POSTGRES_HOST"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    port=os.getenv("POSTGRES_PORT")
)

def DBConnect():
   return dbConnection.cursor()

def DBCommit():
   dbConnection.commit()

def DBclose():
   dbConnection.commit()
   dbConnection.close()