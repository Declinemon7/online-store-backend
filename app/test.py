from fastapi import FastAPI
from app.routers.products import router_products
from app.routers.categories import router_categories
from app.routers.orders import router_orders
from app.database import engine, Base

app = FastAPI()

Base.metadata.create_all(bind=engine) #Создаем таблицы в базе данных (если их нет)

app.include_router(router_products)
app.include_router(router_categories)
app.include_router(router_orders)

