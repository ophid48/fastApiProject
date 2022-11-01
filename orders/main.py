from fastapi import Depends, FastAPI, HTTPException, Security

import orders.crud as crud
import orders.schemas as schemas
from sqlalchemy.orm import Session
from dependencies import get_db, security


from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/orders"
)


@router.get("/", response_model=list[schemas.Order])
async def get_orders(db: Session = Depends(get_db)):
    orders = crud.get_orders(db)
    return orders


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

