from sqlalchemy import Column, Float, Integer, String

from ..database import Base


# SQLAlchemy Product Class/Model
class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    description = Column(String(200))
    price = Column(Float)
    qty = Column(Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty
