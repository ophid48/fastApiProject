from fastapi import Depends, FastAPI, HTTPException, Security

import dependencies
import schemas.order_status as schemas
import status.models as models
from sqlalchemy.orm import Session
from dependencies import get_db, security


from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/status"
)


############################################################
#   CATEGORY CRUD API   ####################################
@router.get("/", tags=["Status"], response_model=list[schemas.Status])
async def get_status(db: Session = Depends(get_db)):
    return dependencies.get(models.Status, db)


@router.post("/", tags=["Status"])
async def post_status(item: schemas.StatusCreate, db: Session = Depends(get_db)):
    return dependencies.post(item, models.Status, db)


@router.put("/{status_id}", tags=["Status"], response_model=schemas.Status)
async def put_status(status_id, item: schemas.StatusCreate, db: Session = Depends(get_db)):
    return dependencies.put(status_id, item, models.Status, db)


@router.delete("/{status_id}", tags=["Status"])
async def delete_status(status_id, db: Session = Depends(get_db)):
    return dependencies.delete(status_id, models.Status, db)
#   CATEGORY CRUD API   ####################################
############################################################
