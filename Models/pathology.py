from pydantic import BaseModel


class Pathology(BaseModel):
    userid: str
    date: str
    test: str
    result: str = ""
    result_file: str = ""

    def to_dict(self):
        return {
            "userid": self.userid,
            "date": self.date,
            "test": self.test,
            "result": self.result,
            "result_file": self.result_file
        }
