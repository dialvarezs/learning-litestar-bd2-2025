from dataclasses import dataclass

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy.orm import Mapped, mapped_column


class User(BigIntAuditBase):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True)
    fullname: Mapped[str]
    password: Mapped[str]


@dataclass
class PasswordUpdate:
    current_password: str
    new_password: str
