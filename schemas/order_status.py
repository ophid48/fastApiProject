from typing import Union, Optional

from pydantic import BaseModel

from schemas.Category_product import Product
from user.schemas import User


class OrderProductBase(BaseModel):
    productid: int
    orderid: int


class StatusBase(BaseModel):
    status_name: str


class StatusCreate(StatusBase):
    pass


class Status(StatusBase):
    id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    address: str
    city: str
    country: str
    zip: str
    statusid: int
    desc: Optional[str] = None


class OrderCreate(OrderBase):
    products: list[int]
    users: list[int]


class Order(OrderBase):
    id: int

    status: Status

    class Config:
        orm_mode = True


class JoinedOrder(Order):
    products: list[Product]
    users: list[User]
