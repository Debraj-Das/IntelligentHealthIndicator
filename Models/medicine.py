from pydantic import BaseModel, ConfigDict


class Medicine(BaseModel):
    userid: int
    date: str
    doctor: str
    medicine: str

    def to_dict(self):
        return {
            "userid": self.userid,
            "date": self.date,
            "doctor": self.doctor,
            "medicine": self.medicine
        }
