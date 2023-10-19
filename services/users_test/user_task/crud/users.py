from user_task.crud.base import CRUDBase
from user_task.models.users import User
from user_task.schemas.users import UserCreate, UserUpdate


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    pass


crud_user = CRUDUser(User)
