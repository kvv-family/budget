from typing import Optional

from pydantic import BaseModel


class UserModel(BaseModel):
    id: int
    provider: str
    full_name: str
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    avatar_url: str
