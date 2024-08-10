from pydantic import BaseModel


class Pathology(BaseModel):
    userid: int
    date: str
    test: str
    result: str


class PathologyUpdate(BaseModel):
    id: int | None = None
    userid: int | None = None
    date: str | None = None
    test: str | None = None
    result: str | None = None
