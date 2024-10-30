from pydantic import BaseModel


class ShopEnv(BaseModel):
    shopid: int
    date: str
    temperature: float
    co2_level: float
    humidity: float
    AQI: float
    light_level: float
    noise_level: float
