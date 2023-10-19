from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any, Optional, List

from user_task import crud
from user_task.api import deps
from user_task.schemas.users import User, UserCreate, UserInDBBase
from user_task.back.random_users import generate

router = APIRouter()


@router.get("/random", status_code=200, response_model=List[UserInDBBase])
def get_all_users_via_random(
        *,
        db: Session = Depends(deps.get_db),
        num: int,
) -> List:
    user_list = generate(num)
    for user_in in user_list:
        crud.crud_user.create(db=db, obj_in=user_in)
    return user_list


@router.get("/", status_code=200, response_model=List[UserInDBBase])
def get_all_users(
        *,
        db: Session = Depends(deps.get_db),
) -> List:
    result = crud.crud_user.get_multi(db=db)
    return result


@router.get("/{id}", status_code=200, response_model=UserInDBBase)
def get_user_by_id(
        *,
        id: int,
        db: Session = Depends(deps.get_db),
) -> dict:
    """
    Search for user based on label keyword
    """
    user = crud.crud_user.get(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} is not found")
    return user


@router.post("/", status_code=201, response_model=UserInDBBase)
def create_user(
        *, user_in: UserCreate, db: Session = Depends(deps.get_db)
) -> dict:
    """
    Create a new user in the database.
    """
    user = crud.crud_user.create(db=db, obj_in=user_in)
    return user


@router.delete("/", status_code=201, response_model=UserInDBBase)
def delete_user(
        *, id: int, db: Session = Depends(deps.get_db)
) -> dict:
    """
    delete a user with id from the database.
    """
    user = crud.crud_user.delete(db=db, id=id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} is not found")
    return user
