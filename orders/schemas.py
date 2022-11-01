from typing import Union, Optional

from pydantic import BaseModel


class OrderBase(BaseModel):
    name: str
    address: str
    city: str
    counry: str
    zip: str
    shipped: bool


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    name: str
    address: str
    city: str
    counry: str
    zip: str
    shipped: bool

    class Config:
        orm_mode = True


