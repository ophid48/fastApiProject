from typing import Union, Optional, List

from pydantic import BaseModel


class CategoryBase(BaseModel):
    category_name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int

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
    id: int

    class Config:
        orm_mode = True


class JoinedCategory(Category):
    products: List[Product]


class JoinedProduct(Product):
    category: Category
