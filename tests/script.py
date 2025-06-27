import requests

car_id = 1  # Substitua pelo ID do carro que você deseja atualizar

data = {
    "brand": "Honda",
    "model": "Civic",
    "color": "Preto",
    "factory_year": 2021,
    "model_year": 2022,
    "description": "Sedan esportivo, motor turbo"
}

response = requests.delete(f"http://localhost:8000/api/v1/cars/{car_id}", json=data)

print(response.json())