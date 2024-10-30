from pydantic import BaseModel


class Pathology(BaseModel):
    userid: int
    date: str
    test: str
    result: str
