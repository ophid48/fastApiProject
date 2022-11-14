from sqlalchemy import MetaData, Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base




class Status(Base):
    __tablename__ = "status"

    id = Column(Integer, primary_key=True, index=True)
    status_name = Column(String)

    orders = relationship("Order", back_populates="status", cascade="all")