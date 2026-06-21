from pydantic import BaseModel
from typing import Optional


class HorseCreate(BaseModel):
    name: str
    breed: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    sire: Optional[str] = None
    dam: Optional[str] = None
    sires_sire: Optional[str] = None
    sires_dam: Optional[str] = None
    dams_sire: Optional[str] = None
    dams_dam: Optional[str] = None


class HorseUpdate(BaseModel):
    name: Optional[str] = None
    breed: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    sire: Optional[str] = None
    dam: Optional[str] = None
    sires_sire: Optional[str] = None
    sires_dam: Optional[str] = None
    dams_sire: Optional[str] = None
    dams_dam: Optional[str] = None


class HorseResponse(BaseModel):
    id: int
    name: str
    breed: Optional[str] = None
    age: Optional[int] = None
    gender: Optional[str] = None
    sire: Optional[str] = None
    dam: Optional[str] = None
    sires_sire: Optional[str] = None
    sires_dam: Optional[str] = None
    dams_sire: Optional[str] = None
    dams_dam: Optional[str] = None
    farm_id: int

    class Config:
        from_attributes = True
