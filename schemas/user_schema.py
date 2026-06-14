from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    is_librarian: bool = False


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    is_librarian: bool

    model_config = {"from_attributes": True}
