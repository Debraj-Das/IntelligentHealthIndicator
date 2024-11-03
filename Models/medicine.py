from pydantic import BaseModel


class Medicine(BaseModel):
    userid: str
    date: str
    doctor: str
    medicine: str = ""
    prescription_file: str = ""

    def to_dict(self):
        return {
            "userid": self.userid,
            "date": self.date,
            "doctor": self.doctor,
            "medicine": self.medicine,
            "prescription_file": self.prescription_file
        }
