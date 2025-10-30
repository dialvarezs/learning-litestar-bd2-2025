from advanced_alchemy.repository import SQLAlchemySyncRepository
from sqlalchemy.orm import Session

from app.models import Book, User


class UserRepository(SQLAlchemySyncRepository[User]):
    """Repository for user database operations."""

    model_type = User


async def provide_user_repo(db_session: Session) -> UserRepository:
    """Provide user repository instance with auto-commit."""
    return UserRepository(session=db_session, auto_commit=True)


class BookRepository(SQLAlchemySyncRepository[Book]):
    """Repository for book database operations."""

    model_type = Book


async def provide_book_repo(db_session: Session) -> BookRepository:
    """Provide book repository instance with auto-commit."""
    return BookRepository(session=db_session, auto_commit=True)
