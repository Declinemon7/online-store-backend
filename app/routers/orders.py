from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from sqlalchemy.orm import Session
from app.schemas import OrderCreate, OrderRead
from app.models import Orders, Products
from typing import List

router_orders = APIRouter(prefix='/Orders', tags=['Orders'])


@router_orders.post('/')
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    product = db.query(Products).filter(Products.id == order.product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail='Товар не создан!')

    total_price = product.price * order.quantity

    new_order = Orders(
        product_id=order.product_id,
        quantity=order.quantity,
        total_price=total_price
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return {'message': f'Заказ успешно создан!'}


@router_orders.get('/', response_model=List[OrderRead])
def get_all_orders(db: Session = Depends(get_db)):
    orders = db.query(Orders).all()

    if not orders:
        raise HTTPException(status_code=404, detail='Список заказов пуст!')

    return orders


@router_orders.get('/{order_id}', response_model=OrderRead)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Orders).filter(Orders.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail='Заказ не найден!')

    return order
