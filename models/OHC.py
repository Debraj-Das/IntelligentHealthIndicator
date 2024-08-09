from pydantic import BaseModel


class OHC(BaseModel):
    userid: int
    date: str
    doctor: str
    prescription: str


class OHCUpdate(BaseModel):
    id: int | None = None
    userid: int | None = None
    date: str | None = None
    doctor: str | None = None
    prescription: str | None = None
