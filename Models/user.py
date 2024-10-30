from pydantic import BaseModel


class User(BaseModel):
    userid: str
    name: str
    password: str
    phone: str
    email: str
    role: str
