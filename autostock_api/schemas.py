from pydantic import BaseModel
from typing import Optional

class CarBase(BaseModel):
    brand: str
    model: str
    color: Optional[str]
    factory_year: Optional[int]
    model_year: Optional[int]
    description: Optional[str]

class CarCreate(CarBase):
    pass

class CarRead(CarBase):
    id: int

    class Config:
        orm_mode = True