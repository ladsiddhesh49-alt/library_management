from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from database.database import Base

class Book(Base):

    __tablename__ = "books"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String(200),
        nullable=False
    )

    author = Column(
        String(100),
        nullable=False
    )

    quantity = Column(
        Integer,
        default=1
    )