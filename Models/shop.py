from pydantic import BaseModel


class Shop(BaseModel):
    shopid: int
    location: str
