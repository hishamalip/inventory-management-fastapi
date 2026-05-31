from fastapi import FastAPI
from models import Product
from database import session, engine
import database_model 

app = FastAPI()

# To create database tables
database_model.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to FastAPI by Hisham"




products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=10),
    Product(id=2, name="laptop", description="gaming laptop", price=123.43, quantity=6),
    Product(id=3, name="mouse", description="wireless mouse", price=52.5, quantity=4)
]


# Intialize database with products
def init_db():
    db = session()

    count = db.query(database_model.Product).count()
    print(count)
    if count == 0:
        for product in products:
            print(product.model_dump)
            db.add(database_model.Product(**product.model_dump()))
        db.commit()

init_db()

# get all products
@app.get("/products/")
def get_all_products():
    db = session()
    query = db.query(Product)
    return query.all()

# get a single product
@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
        
    return "product not found"


# add product
@app.post("/products/")
def add_product(product: Product):
    products.append(product)
    return "product added successfully"


# delete a product
@app.delete("/products/{id}")
def delete_product(id: int):
    for product in products:
        if product.id == id:
            products.remove(product)
            return f"product with id: {id} deleted successfull"
    
    return f"no product with id: {id} found"


# update a product
@app.put("/products/")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product updated successfully"
    
    return f"product with id: {id} not found"
