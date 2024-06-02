# models.py
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str | None=None
    email: str | None=None
    password: str | None=None
