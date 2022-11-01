from sqlalchemy.orm import Session

import orders.models as models
import schemas

import bcrypt


def get_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order).order_by('id').offset(skip).limit(limit).all()


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
