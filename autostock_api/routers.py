from fastapi import APIRouter

router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars'],
)


@router.get('/')
def list_cars():
    return {
        'cars': [
            {'id': 1, 'modelo': 'Renault Kwid'},
            {'id': 2, 'modelo': 'Hyundai HB20'},
            {'id': 3, 'modelo': 'Honda Civic'},
        ]
    }
