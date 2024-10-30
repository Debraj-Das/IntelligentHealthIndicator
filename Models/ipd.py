from pydantic import BaseModel

class IPD(BaseModel):
   userid: int
   admit_no: int
   admission_date: str
   discharge_date: str
   doctor: str
   prescription: str
   status: int

class IPDUpdate(BaseModel):
   id: int | None = None
   userid: int | None = None
   admit_no: int | None = None
   admission_date: str | None = None
   discharge_date: str | None = None
   doctor: str | None = None
   prescription: str | None = None
   status: int | None = None