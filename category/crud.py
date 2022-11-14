from sqlalchemy.orm import Session


from product.models import Product
from category.models import Category


def get_joined_category(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Category).join(Product.category).all()
