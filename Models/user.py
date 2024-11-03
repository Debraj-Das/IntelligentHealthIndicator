from pydantic import BaseModel


class User(BaseModel):
    userid: str
    name: str
    password: str
    phone: str
    email: str
    role: str

    def to_dict(self):
        return {
            "userid": self.userid,
            "name": self.name,
            "password": self.password,
            "phone": self.phone,
            "email": self.email,
            "role": self.role
        }


class WorkDetails(BaseModel):
    userid: str
    shopid: str
    shift: str
    grade: str
    joining_shop: str
    distance_from_residence: str

    def to_dict(self):
        return {
            "userid": self.userid,
            "shopid": self.shopid,
            "shift": self.shift,
            "grade": self.grade,
            "joining_shop": self.joining_shop,
            "distance_from_residence": self.distance_from_residence
        }
