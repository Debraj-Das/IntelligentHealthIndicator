from pydantic import BaseModel


class IPD(BaseModel):
    userid: int
    admit_no: int
    admission_date: str
    discharge_date: str
    doctor: str
    prescription: str
    status: int

    def to_dict(self):
        return {
            "userid": self.userid,
            "admit_no": self.admit_no,
            "admission_date": self.admission_date,
            "discharge_date": self.discharge_date,
            "doctor": self.doctor,
            "prescription": self.prescription,
            "status": self.status
        }
