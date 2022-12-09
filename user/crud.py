from sqlalchemy.orm import Session

import user.models as models
import user.schemas as schemas
from roles.models import Role

import bcrypt


def get_joined_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).join(Role.users).all()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).order_by('user_id').offset(skip).limit(limit).all()


def get_user_by_login(db: Session, login: str):
    return db.query(models.User).filter(models.User.login == login).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def delete_user_by_id(db: Session, user_id: int):
    db.query(models.User).filter(models.User.user_id == user_id).first().delete()
    db.commit()
    return True


def patch_user(db: Session, usur: schemas.UserCreate):
    pass


def create_user(db: Session, user: schemas.UserCreate):
    db_item = models.User(**user.dict())
    salt = bcrypt.gensalt()
    db_item.password = bcrypt.hashpw(str.encode(db_item.password), salt)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
