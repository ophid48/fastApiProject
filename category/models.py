from sqlalchemy import MetaData, Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String)

    products = relationship("Product", back_populates="category", cascade="all")