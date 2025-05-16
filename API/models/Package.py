from pydantic import BaseModel

class DataESP32(BaseModel):
    pin : int

class Package(BaseModel):
    description: str | None = None
    date: str
    time: str
    data : DataESP32
