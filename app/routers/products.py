from fastapi import APIRouter, Depends
from app.database import get_db
from typing import List
from app.crud import *

router_products = APIRouter(prefix='/products', tags=['Products'])


@router_products.post('/')
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return crud_create_product(product, db)


@router_products.get('/', response_model=List[ProductRead])
def get_all_products(db: Session = Depends(get_db)):
    return crud_get_all_products(db)


@router_products.get('/{product_id}', response_model=ProductRead)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return crud_get_product(product_id, db)


@router_products.put('/{product_id}', response_model=ProductRead)
def update_product(product_id: int, product_new: ProductCreate, db: Session = Depends(get_db)):
    return crud_update_product(product_id, product_new, db)


@router_products.delete('/{product_id}')
def del_product(product_id: int, db: Session = Depends(get_db)):
    return crud_del_product(product_id, db)
