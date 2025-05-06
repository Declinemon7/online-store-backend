from sqlalchemy.orm import Session
from app.schemas import *
from app.models import *
from fastapi import HTTPException

# -----------products-----------


def crud_create_product(product: ProductCreate, db: Session):
    product_new = Products(**product.dict())

    db.add(product_new)
    db.commit()
    db.refresh(product_new)

    return {'Продукт создан': product_new}


def crud_get_all_products(db: Session):
    products = db.query(Products).all()

    if not products:
        raise HTTPException(status_code=404, detail='Список продуктов пуст!')

    return products


def crud_get_product(product_id: int, db: Session):
    product = db.query(Products).filter(Products.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail='Продукт не найден!')

    return product


def crud_update_product(product_id: int, product_new: ProductCreate, db: Session):
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


def crud_del_product(product_id: int, db: Session):
    product = db.query(Products).filter(Products.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail='Продукт не найден!')

    db.delete(product)
    db.commit()

    return {'Message': f'Продукт {product.name} успешно удален!'}


# -----------categories----------


def crud_create_category(category: CategoryCreate, db: Session):
    new_category = Categories(**category.dict())

    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return {'message': f'Новая категория {new_category.name} успешно создана!'}


def crud_get_all_categories(db: Session):
    categories = db.query(Categories).all()

    if not categories:
        raise HTTPException(status_code=404, detail='Список категорий пуст!')

    return categories


def crud_get_category(category_id: int, db: Session):
    category = db.query(Categories).filter(Categories.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail='Категория не найдена!')

    return category


def crud_update_category(category_id: int, category_new: CategoryCreate, db: Session):
    category = db.query(Categories).filter(Categories.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail='Категория не найдена!')

    category.name = category_new.name

    db.commit()
    db.refresh(category)

    return category


def crud_del_category(category_id: int, db: Session):
    category = db.query(Categories).filter(Categories.id == category_id).first()

    if not category:
        raise HTTPException(status_code=404, detail='Категория не найдена!')

    db.delete(category)
    db.commit()

    return {'Message': f'Категория {category.name} успешно удалена!'}


# -----------orders----------


def crud_create_order(order: OrderCreate, db: Session):
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


def crud_get_all_orders(db: Session):
    orders = db.query(Orders).all()

    if not orders:
        raise HTTPException(status_code=404, detail='Список заказов пуст!')

    return orders


def crud_get_order(order_id: int, db: Session):
    order = db.query(Orders).filter(Orders.id == order_id).first()

    if not order:
        raise HTTPException(status_code=404, detail='Заказ не найден!')

    return order
