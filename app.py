from dataclasses import asdict, dataclass

from litestar import Controller, Litestar, delete, get, patch, post, put
from litestar.exceptions import HTTPException
from litestar.openapi import OpenAPIConfig
from litestar.openapi.plugins import ScalarRenderPlugin, SwaggerRenderPlugin

openapi_config = OpenAPIConfig(
    title="Mi API",
    version="0.1",
    render_plugins=[
        ScalarRenderPlugin(),
        SwaggerRenderPlugin(),
    ],
)


@dataclass
class User:
    id: int
    username: str
    fullname: str


@dataclass
class UserUpdate:
    id: int | None = None
    username: str | None = None
    fullname: str | None = None


DB_FAKE = {
    1: User(id=1, username="admin", fullname="Admin"),
    2: User(id=2, username="user", fullname="Normal user"),
    3: User(id=3, username="guest", fullname="Guest"),
}


class UserController(Controller):
    path = "/usuarios"

    @get("/")
    async def list_users(self) -> dict[int, User]:
        return DB_FAKE

    @get("/{id:int}")
    async def get_user(self, id: int) -> User:
        if id not in DB_FAKE:
            raise HTTPException(
                detail="Usuario no encontrado",
                status_code=404,
            )

        return DB_FAKE[id]

    @post("/")
    async def create_user(self, data: User) -> User:
        if data.id in DB_FAKE:
            raise HTTPException(
                detail=f"Usuario con id={data.id} ya existe",
                status_code=409,
            )

        DB_FAKE[data.id] = data

        return data

    @put("/{id:int}")
    async def replace_user(self, id: int, data: User) -> User:
        if id not in DB_FAKE:
            raise HTTPException(
                detail="Usuario no encontrado",
                status_code=404,
            )

        data.id = DB_FAKE[id].id
        DB_FAKE[id] = data

        return data
        

    @patch("/{id:int}")
    async def update_user(self, id: int, data: UserUpdate) -> User:
        if id not in DB_FAKE:
            raise HTTPException(
                detail="Usuario no encontrado",
                status_code=404,
            )

        user = DB_FAKE[id]
        for k, v in asdict(data).items():
            if v is not None:
                setattr(user, k, v)

        return user

    @delete("/{id:int}")
    async def delete_user(self, id: int) -> None:
        if id not in DB_FAKE:
            raise HTTPException(
                detail="Usuario no encontrado",
                status_code=404,
            )

        del DB_FAKE[id]


app = Litestar(
    route_handlers=[UserController],
    openapi_config=openapi_config,
    debug=True,
)
