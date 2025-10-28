from app.models import User

FAKE_DB = {
    1: User(id=1, username="admin", fullname="Admin"),
    2: User(id=2, username="user", fullname="Normal user"),
    3: User(id=3, username="guest", fullname="Guest"),
}