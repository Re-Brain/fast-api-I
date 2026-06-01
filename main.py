from fastapi import FastAPI
from database import engine
import models
import uvicorn

app = FastAPI()

# Creates tables if they don't exist
# Tells the session which database to talk to.
models.Base.metadata.create_all(bind=engine)  

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/horses")
def read_horses():
    return {"message": "List of horses"}

@app.get("/horses/{horse_id}")
def read_horse(horse_id: int):
    return {"horse_id": horse_id}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)