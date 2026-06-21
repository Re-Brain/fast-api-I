from pydantic import BaseModel
from typing import Optional


class FarmUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    description: Optional[str] = None
    capacity: Optional[int] = None


class FarmResponse(BaseModel):
    id: int
    name: str
    location: Optional[str] = None
    description: Optional[str] = None
    capacity: Optional[int] = None
    status: str
    owner_id: int

    class Config:
        from_attributes = True
