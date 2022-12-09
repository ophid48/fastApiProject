from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine

import user.main
from user import models as user_model

import product.main
from product import models as product_model

import order.main
from order import models as order_model

import category.main
from category import models as category_model

import status.main
from status import models as status_model

import roles.main
from roles import models as roles_model


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


user_model.Base.metadata.create_all(bind=engine)
product_model.Base.metadata.create_all(bind=engine)
order_model.Base.metadata.create_all(bind=engine)
category_model.Base.metadata.create_all(bind=engine)
status_model.Base.metadata.create_all(bind=engine)
roles_model.Base.metadata.create_all(bind=engine)


app.include_router(user.main.router)
app.include_router(product.main.router)
app.include_router(order.main.router)
app.include_router(category.main.router)
app.include_router(status.main.router)
app.include_router(roles.main.router)

