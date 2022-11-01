from typing import Union, Optional, List

from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    description: str
    price: float


class ProductCreate(ProductBase):
    categoryId: int


class Product(ProductBase):
    id: int
    name: str
    categoryId: int
    description: Optional[str] = None
    price: int

    class Config:
        orm_mode = True


class JoinedProduct(BaseModel):
    product_id: int
    product_name: str
    description: Optional[str] = None
    price: float
    category: Category

    class Config:
        orm_mode = True
