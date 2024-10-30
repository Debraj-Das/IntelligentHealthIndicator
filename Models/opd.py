from pydantic import BaseModel


class OPD(BaseModel):
    userid: int
    date: str
    doctor: str
    prescription: str
    status: int

    def to_dict(self):
        return {
            "userid": self.userid,
            "date": self.date,
            "doctor": self.doctor,
            "prescription": self.prescription,
            "status": self.status
        }
