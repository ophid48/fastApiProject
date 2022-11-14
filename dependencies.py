from fastapi import Depends, APIRouter

from database import SessionLocal
from fastapi.security import HTTPBearer

from sqlalchemy.orm import Session

import crud


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


security = HTTPBearer()


def get(api_model, db: Session = Depends(get_db)):
    items = crud.get_items(db, api_model)
    return items


def get_by_id(item_id, api_model, db: Session = Depends(get_db)):
    items = crud.get_item_by_id(db, api_model, item_id)
    return items


def post(item, api_model, db: Session = Depends(get_db)):
    item = crud.post_item(db, api_model, item)
    return item


def put(item_id, item, api_model, db: Session = Depends(get_db)):
    item = crud.put_item(db, api_model, item, item_id)
    return item


def delete(item_id, api_model, db: Session = Depends(get_db)):
    item = crud.delete_item_by_id(db, api_model, item_id)
    return item

