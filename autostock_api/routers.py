from fastapi import APIRouter, HTTPException, Depends
from autostock_api import schemas, crud, database
from sqlalchemy.orm import Session

router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars'],
)

@router.post('/', response_model=schemas.CarRead)
def create_car(car: schemas.CarCreate, db: Session = Depends(database.get_session)):
    return crud.create_car(db, car)

@router.get('/{car_id}', response_model=schemas.CarRead)
def read_car(car_id: int, db: Session = Depends(database.get_session)):
    car = crud.get_car(db, car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.put('/{car_id}', response_model=schemas.CarRead)
def update_car(car_id: int, car: schemas.CarCreate, db: Session = Depends(database.get_session)):
    car = crud.update_car(db, car_id, car)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car

@router.delete('/{car_id}', response_model=schemas.CarRead)
def delete_car(car_id: int, db: Session = Depends(database.get_session)):
    car = crud.delete_car(db, car_id)
    if car is None:
        raise HTTPException(status_code=404, detail="Car not found")
    return car


@router.get('/')
def list_cars():
    return {
        'cars': [
            {'id': 1, 'modelo': 'Renault Kwid'},
            {'id': 2, 'modelo': 'Hyundai HB20'},
            {'id': 3, 'modelo': 'Honda Civic'},
        ]
    }
