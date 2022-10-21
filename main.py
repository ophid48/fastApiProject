from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordBearer

import crud
import models
import schemas
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

import bcrypt

app = FastAPI()

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


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@app.get("/api/v1/products/", response_model=list[schemas.Product])
async def create_table(db: Session = Depends(get_db)):
    tables = crud.get_products(db)
    return tables


@app.post("/login/")
async def login(user_data: schemas.Login, db: Session = Depends(get_db)):
    if login:
        user = crud.get_user_by_login(db, user_data.login)
        if not user:
            raise HTTPException(status_code=400, detail="Login or pass not found")
        user_data.password = bytes.decode(bcrypt.hashpw(str.encode(user_data.password), str.encode(user.password)))
        if user_data.password == user.password:
            return True
    return False


@app.post("/users/", response_model=schemas.User)
async def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if login:
        user = schemas.User(**crud.create_user(db, user).__dict__)
        return user
    raise HTTPException(status_code=400, detail="Login is already")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/")
async def say_hello(name):
    return {"message": f"Hello {name}"}
