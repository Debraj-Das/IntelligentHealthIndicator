from pydantic import BaseModel


class OHC(BaseModel):
    userid: str
    date: str
    doctor: str
    prescription: str = ""
    prescription_file: str = ""

    def to_dict(self):
        return {
            "userid": self.userid,
            "date": self.date,
            "doctor": self.doctor,
            "prescription": self.prescription,
            "prescription_file": self.prescription_file,
        }
