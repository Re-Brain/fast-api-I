from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models.models as models
from database import get_db

router = APIRouter()

@router.get("/horses")      
def read_horses(db: Session = Depends(get_db)):
    horses = db.query(models.Horse).all()
    return horses

@router.get("/horses/{horse_id}")
def read_horse(horse_id: int, db: Session = Depends(get_db)):  # Depends calls get_db(), grabs the session, and injects it as db
    horse = db.query(models.Horse).filter(models.Horse.id == horse_id).first()
    
    if horse is None:
        raise HTTPException(status_code=404, detail="Horse not found")
    
    return horse