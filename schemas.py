from typing import Union

from pydantic import BaseModel


class TableBase(BaseModel):
    test_column: str


class TableCreate(TableBase):
    pass


class Table(TableBase):
    id: int
    test_column: str

    class Config:
        orm_mode = True
