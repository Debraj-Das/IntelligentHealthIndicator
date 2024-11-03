from pydantic import BaseModel


class OPD(BaseModel):
    userid: str
    date: str
    doctor: str
    prescription: str = ""
    prescription_file: str = ""
    status: str = ""

    def to_dict(self):
        return {
            "userid": self.userid,
            "date": self.date,
            "doctor": self.doctor,
            "prescription": self.prescription,
            "prescription_file": self.prescription_file,
            "status": self.status
        }
