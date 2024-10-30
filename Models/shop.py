from pydantic import BaseModel


class Shop(BaseModel):
    shopid: str
    location: str

    def to_dict(self):
        return {
            "shopid": self.shopid,
            "location": self.location
        }


class ShopEnv(BaseModel):
    shopid: int
    date: str
    temperature: float
    co2_level: float
    humidity: float
    AQI: float
    light_level: float
    noise_level: float

    def to_dict(self):
        return {
            "shopid": self.shopid,
            "date": self.date,
            "temperature": self.temperature,
            "co2_level": self.co2_level,
            "humidity": self.humidity,
            "AQI": self.AQI,
            "light_level": self.light_level,
            "noise_level": self.noise_level
        }
