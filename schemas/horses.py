from pydantic import BaseModel
from typing import Optional, List
from datetime import date


class HorseCreate(BaseModel):
    name: str
    date_of_birth: Optional[date] = None
    color: Optional[str] = None
    gender: Optional[str] = None
    sire: Optional[str] = None
    dam: Optional[str] = None
    sires_sire: Optional[str] = None
    sires_dam: Optional[str] = None
    dams_sire: Optional[str] = None
    dams_dam: Optional[str] = None


class HorseUpdate(BaseModel):
    name: Optional[str] = None
    date_of_birth: Optional[date] = None
    color: Optional[str] = None
    gender: Optional[str] = None
    sire: Optional[str] = None
    dam: Optional[str] = None
    sires_sire: Optional[str] = None
    sires_dam: Optional[str] = None
    dams_sire: Optional[str] = None
    dams_dam: Optional[str] = None


class HorseImageResponse(BaseModel):
    id: int
    image_url: str

    class Config:
        from_attributes = True


class HorseResponse(BaseModel):
    id: int
    name: str
    date_of_birth: Optional[date] = None
    color: Optional[str] = None
    gender: Optional[str] = None
    sire: Optional[str] = None
    dam: Optional[str] = None
    sires_sire: Optional[str] = None
    sires_dam: Optional[str] = None
    dams_sire: Optional[str] = None
    dams_dam: Optional[str] = None
    farm_id: int
    images: List[HorseImageResponse] = []

    class Config:
        from_attributes = True
