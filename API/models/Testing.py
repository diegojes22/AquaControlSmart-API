from pydantic import BaseModel

class Test(BaseModel):
    description : str | None = None
    date : str
    time : str

    