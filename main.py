from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import crud
import schemas

from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Library Management API")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Library Management API"}


@app.post("/users", response_model=schemas.UserResponse)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db)
):
    return crud.create_user(db, user)


@app.get("/users")
def get_users(
    db: Session = Depends(get_db)
):
    return crud.get_users(db)


@app.post("/books", response_model=schemas.BookResponse)
def create_book(
    book: schemas.BookCreate,
    db: Session = Depends(get_db)
):
    return crud.create_book(db, book)


@app.get("/books")
def get_books(
    db: Session = Depends(get_db)
):
    return crud.get_books(db)


@app.post("/borrow")
def borrow_book(
    request: schemas.BorrowBook,
    db: Session = Depends(get_db)
):
    return crud.borrow_book(
        db,
        request.user_id,
        request.book_id
    )


@app.post("/return")
def return_book(
    request: schemas.BorrowBook,
    db: Session = Depends(get_db)
):
    return crud.return_book(
        db,
        request.user_id,
        request.book_id
    )