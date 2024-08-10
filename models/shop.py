from pydantic import BaseModel

class shop(BaseModel):
   shopid: int
   location: str

class shopUpdate(BaseModel):
   shopid: int | None = None
   location: str | None = None
