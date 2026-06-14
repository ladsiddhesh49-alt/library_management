from sqlalchemy.orm import Session

from models.book import Book

class BookRepository:

    @staticmethod
    def create_book(
        db: Session,
        title: str,
        author: str,
        quantity: int
    ):

        book = Book(
            title=title,
            author=author,
            quantity=quantity
        )

        db.add(book)
        db.commit()
        db.refresh(book)

        return book

    @staticmethod
    def get_all_books(
        db: Session
    ):

        return db.query(Book).all()