from routers import Shop, ShopEnv, HumanResource, HRDetails, OccupationalHealthCentre, OPD, IPD, MedicinePrescribed, PathologyTestResults
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
load_dotenv(override=True)


origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Hello World"}


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    if request.url.path not in ["/", "/docs", "/redoc", "/openapi.json"]:
        apiKey = request.headers.get("apiKey")
        if apiKey is None:
            return JSONResponse(status_code=403, content={"message": "API Key is required"})
        if apiKey != os.getenv("APIKEY"):
            return JSONResponse(status_code=403, content={"message": "Invalid API Key"})
    return await call_next(request)


@app.get("/")
def root():
    return {"message": "Health Indicator API Working Successfully"}


app.include_router(Shop.router)
app.include_router(ShopEnv.router)
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
