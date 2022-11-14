from fastapi import Depends, FastAPI, HTTPException, Security

import dependencies
import schemas.Category_product as schemas
import product.crud as crud
import product.models as models
from sqlalchemy.orm import Session
from dependencies import get_db, security


from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/product"
)


@router.get("/joined_products", tags=["Product"], response_model=list[schemas.JoinedProduct])
async def get_joined_products(db: Session = Depends(get_db)):
    products = crud.get_joined_products(db)
    return products


######################################################
#   PRODUCT API   ####################################
@router.get("/", tags=["Product"], response_model=list[schemas.Product])
async def get_products(db: Session = Depends(get_db)):
    return dependencies.get(models.Product, db)


@router.post("/", tags=["Product"])
async def post_product(item: schemas.ProductCreate, db: Session = Depends(get_db)):
    return dependencies.post(item, models.Product, db)


@router.put("/{product_id}", tags=["Product"], response_model=schemas.Product)
async def put_product(product_id, item: schemas.ProductCreate, db: Session = Depends(get_db)):
    return dependencies.put(product_id, item, models.Product, db)


@router.delete("/{product_id}", tags=["Product"])
async def delete_product(product_id, db: Session = Depends(get_db)):
    return dependencies.delete(product_id, models.Product, db)
#   PRODUCT API   ####################################
######################################################


# @router.post("/", response_model=schemas.Product)
# async def post_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
#     category = crud.get_category_by_id(db, product.categoryId)
#     if not category:
#         raise HTTPException(status_code=400, detail="Category not found")
#     new_product = crud.create_product(product, db)
#     return new_product


# @app.post("/signup/")
# async def login(user_data: schemas.Login, db: Session = Depends(get_db)):
#     if login:
#         user = crud.get_user_by_login(db, user_data.login)
#         if not user:
#             raise HTTPException(status_code=400, detail="Login or pass not found")
#         hash_pass = bytes.decode(bcrypt.hashpw(str.encode(user_data.password), str.encode(user.password)))
#         if hash_pass == user.password:
#             access_token = auth.encode_token(hash_pass)
#             return True
#     return False

