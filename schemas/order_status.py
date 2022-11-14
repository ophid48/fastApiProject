from typing import Union, Optional

from pydantic import BaseModel

from schemas.Category_product import Product


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


class OrderCreate(OrderBase):
    products: list[int]


class Order(OrderBase):
    id: int

    status: Status

    class Config:
        orm_mode = True


class JoinedOrder(Order):
    products: list[Product]
