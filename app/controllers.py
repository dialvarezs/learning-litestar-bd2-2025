from typing import Any, Sequence

from advanced_alchemy.exceptions import DuplicateKeyError, NotFoundError
from litestar import Controller, Request, Response, delete, get, patch, post
from litestar.di import Provide
from litestar.dto import DTOData
from litestar.exceptions import HTTPException

from app.dtos import UserCreateDTO, UserReadDTO, UserUpdateDTO
from app.models import PasswordUpdate, User
from app.repositories import UserRepository, provide_user_repo


def not_found_error_handler(_: Request[Any, Any, Any], __: NotFoundError) -> Response[Any]:
    return Response(
        status_code=404,
        content={"status_code": 404, "detail": "User not found"},
    )


def duplicate_error_handler(_: Request[Any, Any, Any], __: DuplicateKeyError) -> Response[Any]:
    return Response(
        status_code=404,
        content={"status_code": 404, "detail": "User already exists"},
    )


class UserController(Controller):
    path = "/usuarios"
    return_dto = UserReadDTO
    dependencies = {"users_repo": Provide(provide_user_repo)}
    exception_handlers = {
        NotFoundError: not_found_error_handler,
        DuplicateKeyError: duplicate_error_handler,
    }

    @get("/")
    async def list_users(self, users_repo: UserRepository) -> Sequence[User]:
        return users_repo.list()

    @get("/{id:int}")
    async def get_user(self, id: int, users_repo: UserRepository) -> User:
        return users_repo.get(id)

    @post("/", dto=UserCreateDTO)
    async def create_user(
        self,
        data: DTOData[User],
        users_repo: UserRepository,
    ) -> User:
        return users_repo.add(data.create_instance())

    @patch("/{id:int}", dto=UserUpdateDTO)
    async def update_user(
        self,
        id: int,
        data: DTOData[User],
        users_repo: UserRepository,
    ) -> User:
        user, _ = users_repo.get_and_update(match_fields="id", id=id, **data.as_builtins())

        return user

    @post("/{id:int}/update-password", status_code=204)
    async def update_password(
        self,
        id: int,
        data: PasswordUpdate,
        users_repo: UserRepository,
    ) -> None:
        user = users_repo.get(id)

        if user.password != data.current_password:
            raise HTTPException(
                detail="Contraseña incorrecta",
                status_code=401,
            )

        user.password = data.new_password
        users_repo.update(user)

    @delete("/{id:int}")
    async def delete_user(self, id: int, users_repo: UserRepository) -> None:
        users_repo.delete(id)
