from typing import Generator

from user_task.db.session import SessionLocal


def get_db() -> Generator:
    db = SessionLocal()
    db.current_user_id = None
    try:
        yield db
    finally:
        db.close()