from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String, nullable=True)
    login = Column(String)
    password = Column(String)
    avatar = Column(String)
    wallpaper = Column(String)
    number = Column(String)
    email = Column(String)
    address = Column(String)
    role_id = Column(Integer, ForeignKey("role.id"))

    role = relationship("Role", back_populates="users")

