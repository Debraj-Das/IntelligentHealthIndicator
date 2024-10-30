from pydantic import BaseModel


class OHC(BaseModel):
    userid: int
    date: str
    doctor: str
    prescription: str
