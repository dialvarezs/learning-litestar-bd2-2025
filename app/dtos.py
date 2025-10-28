from advanced_alchemy.extensions.litestar import SQLAlchemyDTO, SQLAlchemyDTOConfig

from app.models import User


class UserReadDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(exclude={"password"})


class UserCreateDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(
        exclude={"id", "created_at", "updated_at"},
    )


class UserUpdateDTO(SQLAlchemyDTO[User]):
    config = SQLAlchemyDTOConfig(
        exclude={"id", "created_at", "password"},
        partial=True,
    )
