from pydantic import BaseModel

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