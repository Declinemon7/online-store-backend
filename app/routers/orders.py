from fastapi import APIRouter, Depends
from app.database import get_db
from typing import List
from app.crud import *

router_orders = APIRouter(prefix='/Orders', tags=['Orders'])


@router_orders.post('/')
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    return crud_create_order(order, db)


@router_orders.get('/', response_model=List[OrderRead])
def get_all_orders(db: Session = Depends(get_db)):
    return crud_get_all_orders(db)


@router_orders.get('/{order_id}', response_model=OrderRead)
def get_order(order_id: int, db: Session = Depends(get_db)):
    return crud_get_order(order_id, db)
