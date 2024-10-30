from pydantic import BaseModel


class OHC(BaseModel):
    userid: int
    date: str
    doctor: str
    prescription: str

    def to_dict(self):
        return {
            "userid": self.userid,
            "date": self.date,
            "doctor": self.doctor,
            "prescription": self.prescription
        }
