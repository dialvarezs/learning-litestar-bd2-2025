from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig

from app.models import Book, User


class UserReadDTO(SQLAlchemyDTO[User]):
    """DTO for reading user data without password."""

    config = SQLAlchemyDTOConfig(exclude={"password"})


class UserCreateDTO(SQLAlchemyDTO[User]):
    """DTO for creating users."""

    config = SQLAlchemyDTOConfig(
        exclude={"id", "created_at", "updated_at"},
    )


class UserUpdateDTO(SQLAlchemyDTO[User]):
    """DTO for updating users with partial data."""

    config = SQLAlchemyDTOConfig(
        exclude={"id", "created_at", "password"},
        partial=True,
    )


class BookReadDTO(SQLAlchemyDTO[Book]):
    """DTO for reading book data."""

    config = SQLAlchemyDTOConfig()


class BookCreateDTO(SQLAlchemyDTO[Book]):
    """DTO for creating books."""

    config = SQLAlchemyDTOConfig(
        exclude={"id", "created_at", "updated_at"},
    )


class BookUpdateDTO(SQLAlchemyDTO[Book]):
    """DTO for updating books with partial data."""

    config = SQLAlchemyDTOConfig(
        exclude={"id", "created_at", "updated_at"},
        partial=True,
    )
