from advanced_alchemy.repository import SQLAlchemySyncRepository
from sqlalchemy.orm import Session

from app.models import User


class UserRepository(SQLAlchemySyncRepository[User]):
    model_type = User


async def provide_user_repo(db_session: Session) -> UserRepository:
    return UserRepository(session=db_session, auto_commit=True)
