from sqlalchemy.orm import Session

import models
import schemas



def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).order_by('id').offset(skip).limit(limit).all()


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
