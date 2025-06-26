from fastapi import FastAPI

from autostock_api.routers import router as car_router

app = FastAPI(
    title='Autostock API',
    description='Inventory and Sales Management System for Dealerships',
    version='0.1.0',
)

app.include_router(car_router)


@app.get('/')
def read_root():
    return {'status': 'ok'}
