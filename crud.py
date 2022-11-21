from fastapi import HTTPException

from dependencies import Session


def get_items(db: Session, api_model, skip: int = 0, limit: int = 100):
    return db.query(api_model).all()


def get_item_by_id(db: Session, api_model, item_id, skip: int = 0, limit: int = 100):
    return db.query(api_model).filter(api_model.id == item_id).first()


def post_item(db: Session, api_model, item):
    db_item = api_model(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def put_item(db: Session, api_model, item, item_id):
    db_item = get_item_by_id(db, api_model, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Entity not found")
    user_data = item.dict(exclude_unset=True)
    for key, value in user_data.items():
        setattr(db_item, key, value)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item_by_id(db: Session, api_model, item_id):
    db_item = db.query(api_model).filter(api_model.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Entity not found")
    db.delete(db_item)
    db.commit()
    return True

