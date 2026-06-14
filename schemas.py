from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    is_librarian: bool = False


class UserResponse(UserCreate):
    id: int

    class Config:
        from_attributes = True


class BookCreate(BaseModel):
    title: str
    author: str
    isbn: str
    total_copies: int


class BookResponse(BaseModel):
    id: int
    title: str
    author: str
    isbn: str
    total_copies: int
    available_copies: int

    class Config:
        from_attributes = True


class BorrowBook(BaseModel):
    user_id: int
    book_id: int