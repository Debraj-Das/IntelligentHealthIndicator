from pydantic import BaseModel

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