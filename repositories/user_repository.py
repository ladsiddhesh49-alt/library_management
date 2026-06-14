from sqlalchemy.orm import Session

from models.user import User
from schemas.user_schema import UserCreate

class UserRepository:

    @staticmethod
    def create_user(db: Session, user: UserCreate):

        db_user = User(
            name=user.name,
            email=user.email,
            is_librarian=user.is_librarian
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return db_user

    @staticmethod
    def get_all_users(
        db: Session
    ):

        return db.query(User).all()

    @staticmethod
    def get_user_by_id(
        db: Session,
        user_id: int
    ):

        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    @staticmethod
    def delete_user(
        db: Session,
        user_id: int
    ):

        user = (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )

        if user:
            db.delete(user)
            db.commit()

        return user