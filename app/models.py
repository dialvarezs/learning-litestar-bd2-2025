from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    username: str
    fullname: str
    password: str
    created_at: datetime

@dataclass
class PasswordUpdate:
    current_password: str
    new_password: str
