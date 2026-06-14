from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_db
from schemas.user_schema import UserCreate, UserResponse
from services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", response_model=UserResponse)
def create_user(
        user: UserCreate,
        db: Session = Depends(get_db)
):
    return UserService.create_user(db, user)

@router.get("/", response_model=list[UserResponse])
def get_users(
        db: Session = Depends(get_db)
):
    return UserService.get_all_users(db)