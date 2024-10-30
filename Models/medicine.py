from pydantic import BaseModel


class Medicine(BaseModel):
    userid: int
    date: str
    doctor: str
    medicine: str
