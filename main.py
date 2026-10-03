from fastapi import FastAPI

from models import product
app = FastAPI()

@app.get("/")
def greet():
    return "Hello, FastAPI!"

@app.get("/about")
def about():
    return "This is a simple FastAPI application that demonstrates basic routing and response handling."
@app.get("/products")
def get_all_products():
    return [
        {"id": 1, "name": "Product 1", "price": 10.99, "description": "This is product 1."},
        {"id": 2, "name": "Product 2", "price": 19.99, "description": "This is product 2."},
        {"id": 3, "name": "Product 3", "price": 5.99, "description": "This is product 3."},
        {"id": 4, "name": "Product 4", "price": 15.99, "description": "This is product 4."},
    ]