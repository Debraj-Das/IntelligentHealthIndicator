from Routes import mail
from Routes import upload
from fastapi import FastAPI
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from Routes import signin, user, shop, opd, ohc, ipd, medicine, pathology
from fastapi.staticfiles import StaticFiles

app = FastAPI()
load_dotenv(override=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
def root():
    return {"message": os.getenv("SECRET")}


app.include_router(signin.router)
app.include_router(user.router)
app.include_router(shop.router)
app.include_router(opd.router)
app.include_router(ohc.router)
app.include_router(ipd.router)
app.include_router(medicine.router)
app.include_router(pathology.router)
app.include_router(mail.router)


app.include_router(upload.router)
