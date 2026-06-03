from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from database import engine, get_db
import models
import uvicorn

app = FastAPI()

# Add authentication for this branch

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Creates tables if they don't exist
# Tells the session which database to talk to.
models.Base.metadata.create_all(bind=engine)

# Depends calls get_db(), grabs the session, and injects it as db

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/horses")
def read_horses(db: Session = Depends(get_db)):
    horses = db.query(models.Horse).all()
    return horses

@app.get("/horses/{horse_id}")
def read_horse(horse_id: int, db: Session = Depends(get_db)):  # Depends calls get_db(), grabs the session, and injects it as db
    horse = db.query(models.Horse).filter(models.Horse.id == horse_id).first()
    
    if horse is None:
        raise HTTPException(status_code=404, detail="Horse not found")
    
    return horse

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)