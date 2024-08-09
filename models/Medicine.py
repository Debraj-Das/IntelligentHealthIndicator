from pydantic import BaseModel


class Medicine(BaseModel):
    userid: int
    date: str
    doctor: str
    medicine: str


class MedicineUpdate(BaseModel):
    id: int | None = None
    userid: int | None = None
    date: str | None = None
    doctor: str | None = None
    medicine: str | None = None
