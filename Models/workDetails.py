from pydantic import BaseModel


class WorkDetails(BaseModel):
    userid: int
    shopid: int
    shift: str
    grade: str
    joining_shop: str
