from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, Table
from sqlalchemy.orm import relationship

from database import Base


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    city = Column(String)
    country = Column(String)
    zip = Column(String)
    statusid = Column(Integer, ForeignKey("status.id"))

    status = relationship("Status", back_populates="orders")
    products = relationship("Product", secondary="order_product", back_populates='orders')


# order_product = Table('order_product', Base.metadata,
#                       Column('orderid', ForeignKey("order.id")),
#                       Column('productid', ForeignKey("product.id")),
#                       )


class order_product(Base):
    __tablename__ = "order_product"

    orderid = Column(Integer, ForeignKey("order.id"), primary_key=True)
    productid = Column(Integer, ForeignKey("product.id"), primary_key=True)