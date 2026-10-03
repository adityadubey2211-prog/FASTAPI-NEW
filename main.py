from fastapi import FastAPI

from models import product
app = FastAPI()

@app.get("/")
def greet():
    return "Hello, FastAPI!"
products = [
        product(id=1, name="Product 1", price=10.99, description="This is product 1."),
        product(id=2, name="Product 2", price=19.99, description="This is product 2."),
        product(id=3, name="Product 3", price=5.99, description="This is product 3."),
        product(id=4, name="Product 4", price=15.99, description="This is product 4."),
]
@app.get("/products")
def get_products():
    return products

@app.get("/products/{id}")

def get_product(id: int):
    for product in products:
        if product.id == id:
            return product
        
    return {"message": "Product not found."}
        

#add data using post method
@app.post("/products")
def add_product(product: product):
    products.append(product)
    return {"message": "Product added successfully", "product": product}