from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import engine, get_db
import models
import uvicorn

app = FastAPI()

# Creates tables if they don't exist
# Tells the session which database to talk to.
models.Base.metadata.create_all(bind=engine)

# Depends calls get_db(), grabs the session, and injects it as db

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/horses")
def read_horses(db: Session = Depends(get_db)):  
    return db.query(models.Horse).all()

@app.get("/horses/{horse_id}")
def read_horse(horse_id: int, db: Session = Depends(get_db)):  # Depends calls get_db(), grabs the session, and injects it as db
    return db.query(models.Horse).filter(models.Horse.id == horse_id).first()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)