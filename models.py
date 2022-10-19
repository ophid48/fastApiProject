from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Table(Base):
    __tablename__ = "test_table"

    id = Column(Integer, primary_key=True, index=True)
    test_column = Column(String, index=True)
