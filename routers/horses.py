from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session
import models.models as models
from database import get_db
from routers.farms import get_current_farmer
import schemas.horses as horse_schemas

router = APIRouter()


def get_farmer_farm(current_user: models.User = Depends(get_current_farmer), db: Session = Depends(get_db)) -> models.Farm:
    farm = db.query(models.Farm).filter(models.Farm.owner_id == current_user.id).first()
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")
    return farm


@router.get("/horses/me", response_model=list[horse_schemas.HorseResponse])
def get_my_horses(farm: models.Farm = Depends(get_farmer_farm), db: Session = Depends(get_db)):
    return db.query(models.Horse).filter(models.Horse.farm_id == farm.id).all()


@router.post("/horses", response_model=horse_schemas.HorseResponse, status_code=201)
def create_horse(
    data: horse_schemas.HorseCreate,
    farm: models.Farm = Depends(get_farmer_farm),
    db: Session = Depends(get_db),
):
    horse = models.Horse(**data.model_dump(), farm_id=farm.id)
    db.add(horse)
    db.commit()
    db.refresh(horse)
    return horse


@router.patch("/horses/{horse_id}", response_model=horse_schemas.HorseResponse)
def update_horse(
    horse_id: int,
    data: horse_schemas.HorseUpdate,
    farm: models.Farm = Depends(get_farmer_farm),
    db: Session = Depends(get_db),
):
    horse = db.query(models.Horse).filter(models.Horse.id == horse_id).first()
    if not horse:
        raise HTTPException(status_code=404, detail="Horse not found")
    if horse.farm_id != farm.id:
        raise HTTPException(status_code=403, detail="You do not own this horse")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(horse, field, value)

    db.commit()
    db.refresh(horse)
    return horse


@router.delete("/horses/{horse_id}", status_code=204)
def delete_horse(
    horse_id: int,
    farm: models.Farm = Depends(get_farmer_farm),
    db: Session = Depends(get_db),
):
    horse = db.query(models.Horse).filter(models.Horse.id == horse_id).first()
    if not horse:
        raise HTTPException(status_code=404, detail="Horse not found")
    if horse.farm_id != farm.id:
        raise HTTPException(status_code=403, detail="You do not own this horse")

    db.delete(horse)
    db.commit()
    return Response(status_code=204)
