from fastapi import APIRouter, Depends, HTTPException, Response, UploadFile, File
from sqlalchemy.orm import Session
import models.models as models
from database import get_db
from routers.farms import get_current_farmer
from core.cloudinary import upload_image, delete_image
import schemas.horses as horse_schemas

router = APIRouter()


def get_farmer_farm(current_user: models.User = Depends(get_current_farmer), db: Session = Depends(get_db)) -> models.Farm:
    farm = db.query(models.Farm).filter(models.Farm.owner_id == current_user.id).first()
    if not farm:
        raise HTTPException(status_code=404, detail="Farm not found")
    return farm


@router.get("/horses", response_model=list[horse_schemas.HorseResponse])
def get_all_horses(db: Session = Depends(get_db)):
    return db.query(models.Horse).all()


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


@router.get("/horses/{horse_id}", response_model=horse_schemas.HorseResponse)
def get_horse(horse_id: int, db: Session = Depends(get_db)):
    horse = db.query(models.Horse).filter(models.Horse.id == horse_id).first()
    if not horse:
        raise HTTPException(status_code=404, detail="Horse not found")
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


@router.post("/horses/{horse_id}/image", response_model=horse_schemas.HorseResponse)
def upload_horse_image(
    horse_id: int,
    file: UploadFile = File(...),
    farm: models.Farm = Depends(get_farmer_farm),
    db: Session = Depends(get_db),
):
    horse = db.query(models.Horse).filter(models.Horse.id == horse_id).first()
    if not horse:
        raise HTTPException(status_code=404, detail="Horse not found")
    if horse.farm_id != farm.id:
        raise HTTPException(status_code=403, detail="You do not own this horse")
    if len(horse.images) >= 3:
        raise HTTPException(status_code=400, detail="Maximum of 3 images allowed per horse")

    result = upload_image(file.file.read(), folder="horses")
    new_image = models.HorseImage(
        image_url=result["secure_url"],
        image_public_id=result["public_id"],
        horse_id=horse.id,
    )
    db.add(new_image)
    db.commit()
    db.refresh(horse)
    return horse


@router.delete("/horses/{horse_id}/image/{image_id}", response_model=horse_schemas.HorseResponse)
def delete_horse_image(
    horse_id: int,
    image_id: int,
    farm: models.Farm = Depends(get_farmer_farm),
    db: Session = Depends(get_db),
):
    horse = db.query(models.Horse).filter(models.Horse.id == horse_id).first()
    if not horse:
        raise HTTPException(status_code=404, detail="Horse not found")
    if horse.farm_id != farm.id:
        raise HTTPException(status_code=403, detail="You do not own this horse")

    image = db.query(models.HorseImage).filter(
        models.HorseImage.id == image_id,
        models.HorseImage.horse_id == horse_id,
    ).first()
    if not image:
        raise HTTPException(status_code=404, detail="Image not found")

    delete_image(image.image_public_id)
    db.delete(image)
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
