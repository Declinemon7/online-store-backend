from fastapi import APIRouter, Depends
from app.database import get_db
from typing import List
from app.crud import *

router_categories = APIRouter(prefix='/Categories', tags=['Categories'])


@router_categories.post('/')
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    return crud_create_category(category, db)


@router_categories.get('/', response_model=List[CategoryRead])
def get_all_categories(db: Session = Depends(get_db)):
    return crud_get_all_categories(db)


@router_categories.get('/{category_id}', response_model=CategoryRead)
def get_category(category_id: int, db: Session = Depends(get_db)):
    return crud_get_category(category_id, db)


@router_categories.put('/{category_id}', response_model=CategoryRead)
def update_category(category_id: int, category_new: CategoryCreate, db: Session = Depends(get_db)):
    return crud_update_category(category_id, category_new, db)


@router_categories.delete('/{category_id}')
def del_category(category_id: int, db: Session = Depends(get_db)):
    return crud_del_category(category_id, db)
