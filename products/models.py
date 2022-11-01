from sqlalchemy import MetaData, Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Product(Base):
    __tablename__ = "product"

    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String)
    categoryId = Column(Integer, ForeignKey("category.category_id"))
    description = Column(String, nullable=True)
    price = Column(Float)

    category = relationship("Category", back_populates="products")

class Category(Base):
    __tablename__ = "category"

    category_id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String)

    products = relationship("Product", back_populates="category", cascade="all, delete-orphan")


# class JoinedProduct(MetaData):
#     __tablename__ = "JoinedProduct"
#
#     product_id = Column(Integer, primary_key=True, index=True)
#     product_name = Column(String)
#     description = Column(String, nullable=True)
#     price = Column(Float)
#     categoryId = Column(Integer)
#     category_name = Column(String)
