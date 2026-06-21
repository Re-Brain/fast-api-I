from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models.models as models
from database import get_db
from core.auth import decode_token
import schemas.farms as farm_schemas

router = APIRouter()


def get_current_farmer(email: str = Depends(decode_token), db: Session = Depends(get_db)) -> models.User:
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.role != "farmer":
        raise HTTPException(status_code=403, detail="Only farmers can access this resource")
    return user


@router.get("/farms/me", response_model=farm_schemas.FarmResponse)
def get_my_farm(current_user: models.User = Depends(get_current_farmer), db: Session = Depends(get_db)):
    farm = db.query(models.Farm).filter(models.Farm.owner_id == current_user.id).first()
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")
    return farm


@router.patch("/farms/me", response_model=farm_schemas.FarmResponse)
def update_my_farm(
    data: farm_schemas.FarmUpdate,
    current_user: models.User = Depends(get_current_farmer),
    db: Session = Depends(get_db),
):
    farm = db.query(models.Farm).filter(models.Farm.owner_id == current_user.id).first()
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(farm, field, value)

    farm.is_active = all([
        farm.name,
        farm.location,
        farm.description,
        farm.capacity,
    ])

    db.commit()
    db.refresh(farm)
    return farm


@router.get("/farms")
def get_all_farms(db: Session = Depends(get_db)):
    return db.query(models.Farm).filter(models.Farm.is_active == True).all()


@router.get("/farms/{farm_id}")
def get_farm(farm_id: int, db: Session = Depends(get_db)):
    farm = db.query(models.Farm).filter(models.Farm.id == farm_id).first()
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")
    return farm
