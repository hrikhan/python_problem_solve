from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Laptop", "price": 800},
        {"id": 2, "name": "Phone", "price": 500},
        {"id": 3, "name": "Headphones", "price": 150}
    ]


@app.get("/categories")
def get_categories():
    return {
        "Electronics": ["Laptop", "Phone", "Headphones"],
        "Clothing": ["T-shirt", "Jeans", "Shoes"],
        "Books": ["Python 101", "FastAPI Guide", "Data Science"]
    }
