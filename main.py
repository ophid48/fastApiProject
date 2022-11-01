from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine

import user.main
from user import models as user_model

import products.main
from products import models as product_model

import orders.main
from orders import models as order_model


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

app.include_router(user.main.router)
app.include_router(products.main.router)
app.include_router(orders.main.router)
