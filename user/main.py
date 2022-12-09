from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

import auth
import config
import dependencies
import roles.models
import user.crud as crud
import user.models as models
import user.schemas as schemas
from sqlalchemy.orm import Session
from dependencies import get_db, security
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

import bcrypt

from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/users"
)


def check_secret(input_secret):
    return input_secret == config.secret_string


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


@router.post("/login/")
async def login(user_data: schemas.Login, db: Session = Depends(get_db)):
    if login:
        user = crud.get_user_by_login(db, user_data.login)
        if not user:
            raise HTTPException(status_code=400, detail="Login or pass not found")
        hash_pass = bytes.decode(bcrypt.hashpw(str.encode(user_data.password), str.encode(user.password)))
        if hash_pass == user.password:
            access_token = auth.encode_token(hash_pass)
            refresh_token = auth.encode_refresh_token(hash_pass)
            return {'access_token': access_token, 'refresh_token': refresh_token}
        else:
            raise HTTPException(status_code=400, detail="Login or pass not found")
    return False


@router.get('/refresh_token/', tags=["User"])
def refresh_user_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    refresh_token = credentials.credentials
    new_token = auth.decode_refresh_token(refresh_token)
    return {'access_token': new_token}


@router.post("/", tags=["User"], response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    role = dependencies.get_by_id(user.role_id, roles.models.Role, db)
    if not role:
        raise HTTPException(status_code=400, detail="Role not found")
    if user:
        # if auth.decode_token(token, True):
        return crud.create_user(db, user)
        # else:
            # return 'Invalid token'
    raise HTTPException(status_code=400, detail="Login is already")


@router.get("/", tags=["User"], response_model=list[schemas.User])
async def get_users(db: Session = Depends(get_db)):

    # if auth.decode_token(token, True):
    return crud.get_joined_users(db)
    # else:
    #     return 'Invalid token'


@router.delete("/{user_id}", tags=["User"])
async def delete_user(user_id: int, db: Session = Depends(get_db), credentials: HTTPAuthorizationCredentials = Security(security)):
    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return True


@router.patch("/{user_id}", response_model=schemas.User)
async def patch_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    user_data = user.dict(exclude_unset=True)
    if user.password == '':
        user_data["password"] = db_user["password"]
    else:
        salt = bcrypt.gensalt()
        user_data["password"] = bcrypt.hashpw(str.encode(user_data["password"]), salt)
    for key, value in user_data.items():
        setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
