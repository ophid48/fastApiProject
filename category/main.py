from fastapi import Depends, FastAPI, HTTPException, Security

import dependencies
import category.crud as crud
import schemas.Category_product as schemas
import category.models as models
from sqlalchemy.orm import Session
from dependencies import get_db, security


from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/category"
)


@router.get("/joined_category", tags=["Category"], response_model=list[schemas.JoinedCategory])
async def get_joined_category(db: Session = Depends(get_db)):
    products = crud.get_joined_category(db)
    return products


######################################################
#   CATEGORY API   ####################################
@router.get("/", tags=["Category"], response_model=list[schemas.Category])
async def get_categories(db: Session = Depends(get_db)):
    return dependencies.get(models.Category, db)


@router.post("/", tags=["Category"])
async def post_category(item: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return dependencies.post(item, models.Category, db)


@router.put("/{category_id}", tags=["Category"], response_model=schemas.Category)
async def put_category(category_id, item: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return dependencies.put(category_id, item, models.Category, db)


@router.delete("/{category_id}", tags=["Category"])
async def delete_category(category_id, db: Session = Depends(get_db)):
    return dependencies.delete(category_id, models.Category, db)
#   CATEGORY API   ####################################
######################################################