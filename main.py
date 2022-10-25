from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import user.main
from database import engine
from user import models as user_model

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

app.include_router(user.main.router)
