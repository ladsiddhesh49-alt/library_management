from fastapi import FastAPI

from database.database import Base
from database.database import engine

from models.user import User
from models.book import Book

Base.metadata.create_all(bind=engine)

app = FastAPI()