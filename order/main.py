from fastapi import Depends

import schemas.order_status as schemas
import order.models as models
from sqlalchemy.orm import Session

import user.crud
from dependencies import get_db
import dependencies

import order.crud as crud

from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/orders"
)


@router.get("/{order_id}", tags=["Order"], response_model=schemas.JoinedOrder)
async def get_order_by_id(order_id: int, db: Session = Depends(get_db)):
    return crud.get_full_order_by_id(db, order_id)


#######################################################
#   CATEGORY API   ####################################
@router.get("/", tags=["Order"], response_model=list[schemas.JoinedOrder])
async def get_orders(db: Session = Depends(get_db)):
    return crud.get_joined_orders(db)


@router.post("/", tags=["Order"])
async def post_order(item: schemas.OrderCreate, db: Session = Depends(get_db)):
    new_item = schemas.OrderBase(**item.dict())
    new_order = dependencies.post(new_item, models.Order, db)
    crud.post_order_user(db, {
        'order_id': getattr(new_order, 'id'),
        'user_id': item.owner
    })

    for i in item.products:
        crud.post_order_product(db, {
            'productid': i,
            'orderid': new_order.id
        })
    return new_order


@router.put("/{order_id}", tags=["Order"], response_model=schemas.Order)
async def put_order(order_id, item: schemas.OrderCreate, db: Session = Depends(get_db)):
    return dependencies.put(order_id, item, models.Order, db)


@router.patch("/{order_id}", tags=["Order"], response_model=schemas.JoinedOrder)
async def put_order(order_id, item: schemas.OrderPatch, db: Session = Depends(get_db)):
    db_order = dependencies.get_by_id(order_id, models.Order, db)
    order_data = item.dict(exclude_unset=True)
    for key, value in order_data.items():
        if key == 'owner':
            db_order_user = crud.get_order_user(db, getattr(db_order, 'id'), item.owner)
            if db_order_user and getattr(db_order_user, 'user_id'):
                continue
            crud.post_order_user(db, {
                'order_id': getattr(db_order, 'id'),
                'user_id': item.owner
            })
        elif key == 'courier':
            db_order_user = crud.get_order_user(db, getattr(db_order, 'id'), item.courier)
            if db_order_user and getattr(db_order_user, 'user_id'):
                continue
            crud.post_order_user(db, {
                'order_id': getattr(db_order, 'id'),
                'user_id': item.courier
            })
        else:
            setattr(db_order, key, value)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order



@router.delete("/{order_id}", tags=["Order"])
async def delete_order(order_id, db: Session = Depends(get_db)):
    return dependencies.delete(order_id, models.Order, db)
#   CATEGORY API   ####################################
#######################################################
