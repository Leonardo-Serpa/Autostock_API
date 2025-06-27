from typing import Optional

from pydantic import BaseModel


class CarCreate(BaseModel):
    brand: str
    model: str
    color: Optional[str]
    factory_year: Optional[int]
    model_year: Optional[int]
    description: Optional[str]


class CarResponse(BaseModel):
    id: int
    brand: str
    model: str
    color: Optional[str]
    factory_year: Optional[int]
    model_year: Optional[int]
    description: Optional[str]

    class Config:
        orm_mode = True


class CarUpdate(BaseModel):
    brand: str
    model: str
    color: Optional[str]
    factory_year: Optional[int]
    model_year: Optional[int]
    description: Optional[str]
