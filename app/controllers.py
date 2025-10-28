from dataclasses import asdict

from litestar import Controller, delete, get, patch, post, put
from litestar.exceptions import HTTPException

from app.db import FAKE_DB
from app.models import User, UserUpdate


class UserController(Controller):
    path = "/usuarios"

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

    @post("/")
    async def create_user(self, data: User) -> User:
        if data.id in FAKE_DB:
            raise HTTPException(
                detail=f"Usuario con id={data.id} ya existe",
                status_code=409,
            )

        FAKE_DB[data.id] = data

        return data

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
        

    @patch("/{id:int}")
    async def update_user(self, id: int, data: UserUpdate) -> User:
        if id not in FAKE_DB:
            raise HTTPException(
                detail="Usuario no encontrado",
                status_code=404,
            )

        user = FAKE_DB[id]
        for k, v in asdict(data).items():
            if v is not None:
                setattr(user, k, v)

        return user

    @delete("/{id:int}")
    async def delete_user(self, id: int) -> None:
        if id not in FAKE_DB:
            raise HTTPException(
                detail="Usuario no encontrado",
                status_code=404,
            )

        del FAKE_DB[id]