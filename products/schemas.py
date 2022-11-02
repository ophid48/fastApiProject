from typing import Union, Optional, List

from pydantic import BaseModel


class CategoryBase(BaseModel):
    category_name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    category_id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    product_name: str
    description: Optional[str] = None
    price: float
    categoryId: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    product_id: int

    class Config:
        orm_mode = True


class JoinedProduct(Product):
    category: Category


class JoinedCategory(CategoryBase):
    products: List[Product] = []
