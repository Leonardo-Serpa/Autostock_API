from autostock_api import models, schemas
from autostock_api.database import get_session
from autostock_api.schemas import *
from autostock_api.models import Car

def get_car(db: get_session, car_id: int):
    return db.query(models.Car).filter(models.Car.id == car_id).first()

def create_car(db: get_session, car: CarCreate):
    db_car = models.Car(**car.dict())
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car

def update_car(db: get_session, car_id: int, car_update: schemas.CarCreate):
    db_car = db.query(models.Car).filter(Car.id == car_id).first()
    if db_car:
        for key, value in car_update.dict(exclude_unset=True).items():
            setattr(db_car, key, value)
        db.commit()
        db.refresh(db_car)
    return db_car

def delete_car(db: get_session, car_id: int):
    db_car = db.query(models.Car).filter(models.Car.id == car_id).first()
    if db_car:
        db.delete(db_car)
        db.commit()
        db.refresh(db_car)
    return db_car