from pydantic import BaseModel


class Employee(BaseModel):
    userid: int
    name: str
    dob: str
    gender: str
    phone: str
    email: str
    join_date: str | None = None
    leaving_date: str | None = None


class EmployeeUpdate(BaseModel):
    userid: int | None = None
    name: str | None = None
    dob:  str | None = None
    gender: str | None = None
    phone: str | None = None
    email: str | None = None
    join_date: str | None = None
    leaving_date: str | None = None
