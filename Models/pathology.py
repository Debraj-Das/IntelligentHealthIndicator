from pydantic import BaseModel


class Pathology(BaseModel):
    userid: int
    date: str
    test: str
    result: str

    def to_dict(self):
        return {
            "userid": self.userid,
            "date": self.date,
            "test": self.test,
            "result": self.result
        }
