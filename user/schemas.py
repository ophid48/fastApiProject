from typing import Union, Optional

from pydantic import BaseModel

import config
from roles.schemas import Role


class Login(BaseModel):
    login: str
    password: str


class LoginResult(BaseModel):
    result: bool


class UserBase(BaseModel):
    last_name: str
    first_name: Optional[str] = None
    login: str
    password: str
    avatar: Optional[str] = None
    wallpaper: Optional[str] = None
    number: str
    email: str
    address: str


class UserCreate(UserBase):
    role_id: int


class User(UserBase):
    id: int

    role: Role

    class Config:
        orm_mode = True



