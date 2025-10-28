from litestar.dto import DataclassDTO, DTOConfig

from app.models import User


class UserReadDTO(DataclassDTO[User]):
    config = DTOConfig(exclude={"password"})


class UserCreateDTO(DataclassDTO[User]):
    config = DTOConfig(exclude={"id", "created_at"})


class UserUpdateDTO(DataclassDTO[User]):
    config = DTOConfig(
        exclude={"id", "created_at", "password"},
        partial=True,
    )
