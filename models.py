from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    is_librarian = Column(Boolean, default=False)

    transactions = relationship("Transaction", back_populates="user")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    isbn = Column(String, unique=True)
    total_copies = Column(Integer)
    available_copies = Column(Integer)

    transactions = relationship("Transaction", back_populates="book")


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))

    borrow_date = Column(DateTime)
    return_date = Column(DateTime, nullable=True)

    status = Column(String)

    user = relationship("User", back_populates="transactions")
    book = relationship("Book", back_populates="transactions")