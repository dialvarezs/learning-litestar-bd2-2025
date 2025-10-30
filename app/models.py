from dataclasses import dataclass

from advanced_alchemy.base import BigIntAuditBase
from sqlalchemy.orm import Mapped, mapped_column


class User(BigIntAuditBase):
    """User model with audit fields."""

    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True)
    fullname: Mapped[str]
    password: Mapped[str]


@dataclass
class PasswordUpdate:
    """Password update request."""

    current_password: str
    new_password: str
