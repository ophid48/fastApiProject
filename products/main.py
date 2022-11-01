from fastapi import Depends, FastAPI, HTTPException, Security

import products.crud as crud
import products.schemas as schemas
from sqlalchemy.orm import Session
from dependencies import get_db, security


from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/products"
)


@router.get("/joined_products")
async def get_products(db: Session = Depends(get_db)):
    products = crud.get_joined_products(db)

    for i in products:
        print(i.category)
    return products


@router.get("/categories", response_model=list[schemas.Category])
async def get_products(db: Session = Depends(get_db)):
    products = crud.get_categories(db)
    return products


@router.post("/categories", response_model=schemas.Category)
async def get_products(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    products = crud.create_category(category, db)
    return products


@router.post("/", response_model=schemas.Product)
async def post_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    category = crud.get_category_by_id(db, product.categoryId)
    if not category:
        raise HTTPException(status_code=400, detail="Category not found")
    new_product = crud.create_product(product, db)
    return new_product


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

