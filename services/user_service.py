from sqlalchemy.orm import Session
from repositories.user_repository import UserRepository
from schemas.user_schema import UserCreate

class UserService:

    @staticmethod
    def create_user(db: Session, user: UserCreate):
        return UserRepository.create_user(db, user)

    @staticmethod
    def get_all_users(db: Session):
        return UserRepository.get_all_users(db)

    @staticmethod
    def get_user_by_id(db: Session, user_id: int):
        return UserRepository.get_user_by_id(db, user_id)