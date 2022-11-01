from database import SessionLocal
from fastapi.security import HTTPBearer


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


security = HTTPBearer()
