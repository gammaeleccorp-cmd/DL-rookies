from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import date, timedelta
from typing import Optional
import random


app = FastAPI(title="Store API")


class ProductCreate(BaseModel):
    price: float = Field(gt=0)
    expiration_date: date


class ProductUpdate(BaseModel):
    price: Optional[float] = Field(default=None, gt=0)
    expiration_date: Optional[date] = None


def generate_products(count=10):
    products = []

    for product_id in range(1, count + 1):
        products.append(
            {
                "id": product_id,
                "price": round(random.uniform(10, 1000), 2),
                "expiration_date": date.today() + timedelta(days=random.randint(30, 720))
            }
        )

    return products


products = generate_products(10)
next_id = len(products) + 1


@app.get("/")
def read_root():
    return {
        "store": "Simple Store API",
        "products_endpoint": "/products"
    }


@app.get("/products")
def get_products():
    return {
        "data": products
    }


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return {
                "data": product
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


@app.post("/products", status_code=201)
def create_product(product: ProductCreate):
    global next_id

    new_product = {
        "id": next_id,
        "price": product.price,
        "expiration_date": product.expiration_date
    }

    products.append(new_product)
    next_id += 1

    return {
        "data": new_product
    }


@app.put("/products/{product_id}")
def replace_product(product_id: int, product: ProductCreate):
    for index, item in enumerate(products):
        if item["id"] == product_id:
            products[index] = {
                "id": product_id,
                "price": product.price,
                "expiration_date": product.expiration_date
            }

            return {
                "data": products[index]
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


@app.patch("/products/{product_id}")
def update_product(product_id: int, product: ProductUpdate):
    for product_item in products:
        if product_item["id"] == product_id:
            if product.price is not None:
                product_item["price"] = product.price

            if product.expiration_date is not None:
                product_item["expiration_date"] = product.expiration_date

            return {
                "data": product_item
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, item in enumerate(products):
        if item["id"] == product_id:
            deleted_product = products.pop(index)

            return {
                "message": "Product deleted",
                "data": deleted_product
            }

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )
