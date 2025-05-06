from pydantic import BaseModel
from decimal import Decimal


# --------------Категория---------------------
class CategoryCreate(BaseModel):
    name: str


class CategoryRead(BaseModel):
    id: int
    name: str

    model_config = {             # встроенный механизм Pydantic для настройки поведения модели
        "from_attributes": True
    }


# -----------------Товар------------------------
class ProductCreate(BaseModel):
    name: str
    description: str | None = None
    price: Decimal
    category_id: int


class ProductRead(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: Decimal
    category_id: int

    model_config = {
        "from_attributes": True
    }


# -----------------Заказ---------------------
class OrderCreate(BaseModel):
    product_id: int
    quantity: int


class OrderRead(BaseModel):
    id: int
    product_id: int
    quantity: int
    total_price: Decimal

    model_config = {
        "from_attributes": True
    }
