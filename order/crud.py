from sqlalchemy.orm import Session, joinedload

import order.models as models
from status.models import Status


def get_joined_orders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Order)\
        .options(joinedload(models.Order.products))\
        .options(joinedload(models.Order.users)).all()


def get_full_order_by_id(db: Session, item_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Order)\
        .options(joinedload(models.Order.products)).\
        where(models.Order.id == item_id).one()


def post_order_product(db: Session, item):
    db_item = models.order_product(**item)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
