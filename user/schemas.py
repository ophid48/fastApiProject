from typing import Union, Optional

from pydantic import BaseModel

import config


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


class UserCreate(UserBase):
    pass


class User(UserBase):
    user_id: int
    last_name: str
    first_name: Optional[str] = None
    login: str
    password: str

    class Config:
        orm_mode = True



