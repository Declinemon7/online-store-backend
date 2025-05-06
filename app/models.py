from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Categories(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    products = relationship("Products", back_populates="category")


class Products(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Numeric(10, 2))
    category_id = Column(Integer, ForeignKey('category.id'), index=True)

    category = relationship('Categories', back_populates='products')
    orders = relationship('Orders', back_populates='product')


class Orders(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('product.id'), index=True)
    quantity = Column(Integer)
    total_price = Column(Numeric(10, 2))

    product = relationship('Products', back_populates='orders')
