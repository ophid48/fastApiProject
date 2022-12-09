from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    role_name = Column(String)

    users = relationship("User", back_populates="role", cascade="all")
