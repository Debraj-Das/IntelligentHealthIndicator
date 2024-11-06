from pydantic import BaseModel


class User(BaseModel):
    userid: str
    name: str
    password: str
    phone: str
    email: str
    role: str
    shop: str
    joining_date: str
    dob: str
    gender: str

    def to_dict(self):
        return {
            "userid": self.userid,
            "name": self.name,
            "password": self.password,
            "phone": self.phone,
            "email": self.email,
            "role": self.role,
            "shop": self.shop,
            "joining_date": self.joining_date,
            "dob": self.dob,
            "gender": self.gender
        }


class WorkDetails(BaseModel):
    userid: str
    shopid: str
    shift: str
    grade: str
    joining_date: str
    distance_from_residence: str

    def to_dict(self):
        return {
            "userid": self.userid,
            "shopid": self.shopid,
            "shift": self.shift,
            "grade": self.grade,
            "joining_date": self.joining_date,
            "distance_from_residence": self.distance_from_residence
        }
