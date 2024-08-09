from routers import Shop, HumanResource, HRDetails, OccupationalHealthCentre, OPD, IPD, MedicinePrescribed, PathologyTestResults
from fastapi import FastAPI
import os
from dotenv import load_dotenv

app = FastAPI()
load_dotenv()


@app.get("/")
def root():
    return {"message": "FastAPI is working perfectly"}


app.include_router(Shop.router)
app.include_router(HumanResource.router)
app.include_router(HRDetails.router)
app.include_router(OccupationalHealthCentre.router)
app.include_router(OPD.router)
app.include_router(IPD.router)
app.include_router(MedicinePrescribed.router)
app.include_router(PathologyTestResults.router)


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", "8000"))
    host = os.getenv("HOST", "127.0.0.1")
    uvicorn.run(app, host=host, port=port)
