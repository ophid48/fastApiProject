from fastapi import Depends, FastAPI, HTTPException
import crud
import models
import schemas
from sqlalchemy.orm import Session
from database import SessionLocal, engine

from uuid import uuid4

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


models.Base.metadata.create_all(bind=engine)


@app.post("/tables/", response_model=schemas.Table)
async def create_table(table: schemas.TableCreate, db: Session = Depends(get_db)):
    db_table = crud.get_tables_by_column_name(db, table.test_column)
    if db_table:
        raise HTTPException(status_code=400, detail="Email is already")
    return crud.create_table_item(db=db, item=table)


@app.get("/tables/", response_model=list[schemas.Table])
async def create_table(db: Session = Depends(get_db)):
    tables = crud.get_tables(db)
    return tables


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/")
async def say_hello(name):
    return {"message": f"Hello {name}"}
