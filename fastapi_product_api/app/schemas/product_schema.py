from pydantic import BaseModel


# Pydantic models
class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    qty: int

    class Config:
        arbitrary_types_allowed = True


class Status(BaseModel):
    message: str
