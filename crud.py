from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime

import models
import schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db: Session):
    return db.query(models.User).all()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        author=book.author,
        isbn=book.isbn,
        total_copies=book.total_copies,
        available_copies=book.total_copies
    )

    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book


def get_books(db: Session):
    return db.query(models.Book).all()


def borrow_book(db: Session, user_id: int, book_id: int):

    book = db.query(models.Book).filter(
        models.Book.id == book_id
    ).first()

    if not book:
        raise HTTPException(404, "Book not found")

    if book.available_copies <= 0:
        raise HTTPException(400, "No copies available")

    transaction = models.Transaction(
        user_id=user_id,
        book_id=book_id,
        borrow_date=datetime.utcnow(),
        status="borrowed"
    )

    book.available_copies -= 1

    db.add(transaction)
    db.commit()

    return {"message": "Book borrowed successfully"}


def return_book(db: Session, user_id: int, book_id: int):

    transaction = db.query(models.Transaction).filter(
        models.Transaction.user_id == user_id,
        models.Transaction.book_id == book_id,
        models.Transaction.status == "borrowed"
    ).first()

    if not transaction:
        raise HTTPException(404, "Borrow record not found")

    book = db.query(models.Book).filter(
        models.Book.id == book_id
    ).first()

    transaction.status = "returned"
    transaction.return_date = datetime.utcnow()

    book.available_copies += 1

    db.commit()

    return {"message": "Book returned successfully"}