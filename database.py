from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://admin:admin@NIKITA-PC/test?driver=SQL+Server+Native+Client+11.0"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, encoding='latin1', echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
