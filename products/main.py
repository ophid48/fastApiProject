from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

import auth
import config
import crud
import models
import schemas
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

import bcrypt

from fastapi import APIRouter

router = APIRouter(
    prefix="api/users"
)

app = FastAPI()

security = HTTPBearer()

origins = [
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


models.Base.metadata.create_all(bind=engine)

# @app.post("/tables/", response_model=schemas.Table)
# async def create_table(table: schemas.TableCreate, db: Session = Depends(get_db)):
#     db_table = crud.get_tables_by_column_name(db, table.test_column)
#     if db_table:
#         raise HTTPException(status_code=400, detail="Email is already")
#     return crud.create_table_item(db=db, item=table)
#
#
# @app.get("/tables/", response_model=list[schemas.Table])
# async def create_table(db: Session = Depends(get_db)):
#     tables = crud.get_tables(db)
#     return tables


def check_secret(input_secret):
    return input_secret == config.secret_string


@router.get("/api/v1/products/", response_model=list[schemas.Product])
async def create_table(db: Session = Depends(get_db)):
    tables = crud.get_products(db)
    return tables


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


@router.post("/api/v1/login/")
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


@router.get('/refresh_token/')
def refresh_user_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    refresh_token = credentials.credentials
    new_token = auth.decode_refresh_token(refresh_token)
    return {'access_token': new_token}


@router.post("/users/", response_model=schemas.User)
async def login(user: schemas.UserCreate, db: Session = Depends(get_db), credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    if user:
        if auth.decode_token(token, True):
            user = schemas.User(**crud.create_user(db, user).__dict__)
            return user
        else:
            return 'Invalid token'
    raise HTTPException(status_code=400, detail="Login is already")


@router.get("/api/v1/users/", response_model=list[schemas.User])
async def login(db: Session = Depends(get_db), credentials: HTTPAuthorizationCredentials = Security(security)):
    token = credentials.credentials
    print(token)
    if auth.decode_token(token, True):
        users = crud.get_users(db)
        return users
    else:
        return 'Invalid token'


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/")
async def say_hello(name):
    return {"message": f"Hello {name}"}
