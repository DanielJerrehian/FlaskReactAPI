from pydantic import BaseModel
from typing import Optional


class UserValidationSchema(BaseModel):
    name: Optional[str]
    age: Optional[int] = None
    favorite_color: str = None
    
    class Config:
        orm_mode = True