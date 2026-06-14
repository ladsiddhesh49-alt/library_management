from fastapi import FastAPI
from database.database import Base, engine
from models.user import User
from models.book import Book
from api.user_routes import router as user_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "Library Management API Running"}