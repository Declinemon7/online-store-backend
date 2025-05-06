from fastapi import APIRouter, Depends, HTTPException
from app.models import Products
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ProductCreate, ProductRead
from typing import List

router_products = APIRouter(prefix='/products', tags=['Products'])


@router_products.post('/')
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    product_new = Products(**product.dict())

    db.add(product_new)
    db.commit()
    db.refresh(product_new)

    return {'Продукт создан': product_new}


@router_products.get('/', response_model=List[ProductRead])
def get_all_products(db: Session = Depends(get_db)):
    products = db.query(Products).all()

    if not products:
        raise HTTPException(status_code=404, detail='Список продуктов пуст!')

    return products


@router_products.get('/{product_id}', response_model=ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Products).filter(Products.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail='Продукт не найден!')

    return product


@router_products.put('/{product_id}', response_model=ProductRead)
def update_product(product_id: int, product_new: ProductCreate, db: Session = Depends(get_db)):
    product = db.query(Products).filter(Products.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail='Продукт не найден!')

    product.name = product_new.name
    product.description = product_new.description
    product.price = product_new.price
    product.category_id = product_new.category_id

    db.commit()
    db.refresh(product)

    return product


@router_products.delete('/{product_id}')
def del_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Products).filter(Products.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail='Продукт не найден!')

    db.delete(product)
    db.commit()

    return {'Message': f'Продукт {product.name} успешно удален!'}




