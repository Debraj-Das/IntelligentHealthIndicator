from pydantic import BaseModel

class shop(BaseModel):
   shopid: int
   location: str

class shopUpdate(BaseModel):
   shopid: int | None = None
   location: str | None = None

class shopEnviroment(BaseModel):
   shopid: int
   date: str
   temperature: float
   co2_level: float
   humidity: float

class shopEnviromentUpdate(BaseModel):
   id: int | None = None
   shopid: int | None = None
   date: str | None = None
   temperature: float | None = None
   co2_level: float | None = None
   humidity: float | None = None