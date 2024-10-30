from pydantic import BaseModel


class OPD(BaseModel):
    userid: int
    date: str
    doctor: str
    prescription: str
    status: int
