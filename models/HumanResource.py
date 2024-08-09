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


class EmployeeDetails(BaseModel):
    userid: int
    shopid: int
    shift: str
    grade: str
    joining_shop: str


class EmployeeDetailsUpdate(BaseModel):
    id: int | None = None
    userid: int | None = None
    shopid: int | None = None
    shift: str | None = None
    grade: str | None = None
    joining_shop: str | None = None
