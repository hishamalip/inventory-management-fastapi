from fastapi import FastAPI, Depends
from models import Product
from database import session, engine
import database_model
from sqlalchemy.orm import Session

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


# Create get db dependency
def get_db():
    db = session()

    try:
        yield db
    finally:
        db.close()


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


# Intialize db
init_db()


# get all products
@app.get("/products/")
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_model.Product).all()
    return db_products


# get a single product
@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        return db_product
    return "product not found"


# add product
@app.post("/products/")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return "product added successfully"


# update a product
@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "product updated successfully"
    
    return f"product with id: {id} not found"


# delete a product
@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return f"product with id: {id} deleted successfull"
    
    return f"product with id: {id} not found"

