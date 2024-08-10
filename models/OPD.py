from pydantic import BaseModel


class OPD(BaseModel):
    userid: int
    date: str
    doctor: str
    prescription: str
    status: int


class OPDUpdate(BaseModel):
    id: int | None = None
    userid: int | None = None
    date: str | None = None
    doctor: str | None = None
    prescription: str | None = None
    status: int | None = None
