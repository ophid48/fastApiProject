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


class Login(BaseModel):
    login: str
    password: str


class LoginResult(BaseModel):
    result: bool


class UserBase(BaseModel):
    LastName: str
    FirstName: Optional[str] = None
    login: str
    password: str


class UserCreate(UserBase):
    pass


class User(BaseModel):
    id: int
    LastName: str
    FirstName: Optional[str] = None
    login: str
    password: str



