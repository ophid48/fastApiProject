from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

import auth
import config
import dependencies
import user.crud as crud
import roles.models as models
import roles.schemas as schemas
from sqlalchemy.orm import Session
from dependencies import get_db, security
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

import bcrypt

from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/roles"
)


####################################################
#   ROLES API   ####################################
@router.get("/", tags=["Role"], response_model=list[schemas.Role])
async def get_products(db: Session = Depends(get_db)):
    return dependencies.get(models.Role, db)


@router.post("/", tags=["Role"], response_model=schemas.Role)
async def post_product(item: schemas.RoleCreate, db: Session = Depends(get_db)):
    return dependencies.post(item, models.Role, db)


@router.put("/{product_id}", tags=["Role"], response_model=schemas.Role)
async def put_product(product_id, item: schemas.RoleCreate, db: Session = Depends(get_db)):
    return dependencies.put(product_id, item, models.Role, db)


@router.delete("/{product_id}", tags=["Role"])
async def delete_product(product_id, db: Session = Depends(get_db)):
    return dependencies.delete(product_id, models.Role, db)
#   ROLES API   ####################################
####################################################
