from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from autostock_api.database import get_session
from autostock_api.models import Car
from autostock_api.schemas import CarCreate, CarResponse, CarUpdate

router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars'],
)


@router.post('/', response_model=CarResponse)
def create_car(car: CarCreate, db: Session = Depends(get_session)):
    db_car = Car(
        brand = car.brand,
        model = car.model,
        color = car.color,
        factory_year = car.factory_year,
        model_year = car.model_year,
        description = car.description,
    )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


@router.get('/', response_model=List[CarResponse])
def read_cars(
    skip: int = 0, limit: int = 10, db: Session = Depends(get_session)
):
    db_car = db.query(Car).offset(skip).limit(limit).all()
    return db_car


@router.get('/{car_id}', response_model=CarResponse)
def read_car(car_id: int, db: Session = Depends(get_session)):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if db_car is None:
        raise HTTPException(status_code=404, detail='Car not found')
    return db_car


@router.put('/{car_id}', response_model=CarResponse)
def update_car(
    car_id: int, car: CarUpdate, db: Session = Depends(get_session)
):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if db_car is None:
        raise HTTPException(status_code=404, detail='Car not found')

    db_car.brand = car.brand if car.brand is not None else db_car.brand
    db_car.model = car.model if car.model is not None else db_car.model

    db.commit()
    db.refresh(db_car)

    return car


@router.delete('/{car_id}', response_model=CarResponse)
def delete_car(car_id: int, db: Session = Depends(get_session)):
    db_car = db.query(Car).filter(Car.id == car_id).first()
    if db_car is None:
        raise HTTPException(status_code=404, detail='Car not found')
    else:
        db.delete(db_car)
        db.commit()
        db.refresh(db_car)
    return db_car
