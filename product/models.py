from sqlalchemy import MetaData, Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String)
    categoryId = Column(Integer, ForeignKey("category.id"))
    description = Column(String, nullable=True)
    price = Column(Float)

    category = relationship("Category", back_populates="products")
    orders = relationship("Order", secondary="order_product", back_populates='products')
