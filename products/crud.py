from sqlalchemy.orm import Session

import products.models as models
import products.schemas as schemas

import bcrypt


def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).join(models.Category).all()


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).order_by('category_id').offset(skip).limit(limit).all()


def get_joined_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).all()


def get_category_by_id(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def create_product(product: schemas.ProductCreate, db: Session):
    db_item = models.Product(**product.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def create_category(category: schemas.CategoryCreate, db: Session, skip: int = 0, limit: int = 100):
    db_item = models.Category(**category.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# def get_tables_by_column_name(db: Session, name):
#     return db.query(models.Table).filter(models.Table.test_column == name).first()
#
#
# def create_table_item(db: Session, item: schemas.TableCreate):
#     db_item = models.Table(**item.dict())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
