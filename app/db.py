from datetime import datetime

from app.models import User

FAKE_DB = {
    1: User(
        id=1,
        username="admin",
        fullname="Admin",
        password="admin123",
        created_at=datetime.now(),
    ),
    2: User(
        id=2,
        username="user",
        fullname="Normal user",
        password="user111",
        created_at=datetime.now(),
    ),
    3: User(
        id=3,
        username="guest",
        fullname="Guest",
        password="guest",
        created_at=datetime.now(),
    ),
}
