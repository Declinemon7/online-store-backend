from fastapi import APIRouter, Depends, HTTPException
from app.schemas import CategoryCreate, CategoryRead
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Categories
from typing import List

router_categories = APIRouter(prefix='Products')


@router_categories.post('/')
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    new_category = Categories(**category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return {'message': f'Новая категория {new_category.name} успешно создана!'}


@router_categories.get('/', response_model=List[CategoryRead])
def get_all_categories(db: Session = Depends(get_db)):
    categories = db.query(Categories).all()
    return categories


@router_categories.get('/{category_id}', response_model=CategoryRead)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Categories).filter(Categories.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail='Категория не найдена!')
    return category


@router_categories.put('/{category_id}', response_model=CategoryRead)
def edit_category(category_id: int, category_new: CategoryCreate, db: Session = Depends(get_db)):
    category = db.query(Categories).filter(Categories.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail='Категория не найдена!')
    category.name = category_new.name
    db.commit()
    db.refresh(category)
    return category


@router_categories.delete('/{category_id}')
def del_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Categories).filter(Categories.id == category_id).first()
    if not category:
        HTTPException(status_code=404, detail='Категория не найдена!')
    db.delete(category)
    db.commit()
    return {'Message': f'Категория {category.name} успешно удалена!'}




