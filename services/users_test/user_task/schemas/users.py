from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    sex: bool
    age: int
    name: str
    surname: str
    father_name: Optional[str]
    address: str
    e_mail: Optional[str]
    login: str


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


# Properties shared by models stored in DB
class UserInDBBase(UserBase):
    id: int

    class Config:
        orm_mode = True


# Properties to return to client
class User(UserInDBBase):
    pass


# Properties properties stored in DB
class UserInDB(UserInDBBase):
    pass