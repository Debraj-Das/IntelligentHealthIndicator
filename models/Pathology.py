from pydantic import BaseModel


class pathology(BaseModel):
    userid: int
    date: str
    test: str
    result: str


class pathologyUpdate(BaseModel):
    id: int | None = None
    userid: int | None = None
    date: str | None = None
    test: str | None = None
    result: str | None = None
