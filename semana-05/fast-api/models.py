from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import Optional, List
from enum import Enum

class Role(str, Enum):
    roles = ["admin", "student", "instructor"]

class User(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    email: str
    password: str
    role: str

