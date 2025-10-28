from datetime import datetime
from random import randint

from litestar import Controller, Response, delete, get, patch, post, put
from litestar.dto import DTOData
from litestar.exceptions import HTTPException

from app.db import FAKE_DB
from app.dtos import UserCreateDTO, UserReadDTO, UserUpdateDTO
from app.models import PasswordUpdate, User


class UserController(Controller):
    path = "/usuarios"
    return_dto = UserReadDTO

    @get("/")
    async def list_users(self) -> dict[int, User]:
        return FAKE_DB

    @get("/{id:int}")
    async def get_user(self, id: int) -> User:
        if id not in FAKE_DB:
            raise HTTPException(
                detail="Usuario no encontrado",
                status_code=404,
            )

        return FAKE_DB[id]

    @post("/", dto=UserCreateDTO)
    async def create_user(self, data: DTOData[User]) -> User:
        usuario = data.create_instance(
            id=randint(1, 100_000),
            created_at=datetime.now(),
        )

        if usuario.id in FAKE_DB:
            raise HTTPException(
                detail=f"Usuario con id={usuario.id} ya existe",
                status_code=409,
            )

        FAKE_DB[usuario.id] = usuario

        return usuario

    @put("/{id:int}")
    async def replace_user(self, id: int, data: User) -> User:
        if id not in FAKE_DB:
            raise HTTPException(
                detail="Usuario no encontrado",
                status_code=404,
            )

        data.id = FAKE_DB[id].id
        FAKE_DB[id] = data

        return data

    @patch("/{id:int}", dto=UserUpdateDTO)
    async def update_user(self, id: int, data: DTOData[User]) -> User:
        if id not in FAKE_DB:
            raise HTTPException(
                detail="Usuario no encontrado",
                status_code=404,
            )

        user = FAKE_DB[id]
        data.update_instance(user)

        return user

    @post("/{id:int}/update-password", status_code=204)
    async def update_password(self, id: int, data: PasswordUpdate) -> None:
        if id not in FAKE_DB:
            raise HTTPException(
                detail="Usuario no encontrado",
                status_code=404,
            )

        usuario = FAKE_DB[id]

        if usuario.password != data.current_password:
            raise HTTPException(
                detail="Contraseña incorrecta",
                status_code=401,
            )

        usuario.password = data.new_password

    @delete("/{id:int}")
    async def delete_user(self, id: int) -> None:
        if id not in FAKE_DB:
            raise HTTPException(
                detail="Usuario no encontrado",
                status_code=404,
            )

        del FAKE_DB[id]
