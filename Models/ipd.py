from pydantic import BaseModel


class IPD(BaseModel):
    userid: str
    admit_no: str
    admission_date: str
    discharge_date: str
    doctor: str
    prescription: str = ""
    prescription_file: str = ""
    status: str = ""

    def to_dict(self):
        return {
            "userid": self.userid,
            "admit_no": self.admit_no,
            "admission_date": self.admission_date,
            "discharge_date": self.discharge_date,
            "doctor": self.doctor,
            "prescription": self.prescription,
            "prescription_file": self.prescription_file,
            "status": self.status
        }
