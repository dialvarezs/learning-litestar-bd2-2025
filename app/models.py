
from dataclasses import dataclass


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