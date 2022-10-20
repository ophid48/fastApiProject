from typing import Union, Optional

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    category: str
    description: str
    price: float


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    name: str
    category: str
    description: Optional[str] = None
    price: int

    class Config:
        orm_mode = True
