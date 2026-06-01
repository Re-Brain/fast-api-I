from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load the database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# The actual connection to the database
engine = create_engine(DATABASE_URL) 

# Used to open/close sessions with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creates a base class that SQLAlchemy uses to track all your models.
Base = declarative_base()

# Create a session for each request and close it when the request is finished.
# so we don't need to use this everytime when we want to talk to the database.
def get_db():
    db = SessionLocal()  # 1. open a session
    try:
        yield db          # 2. hand it to your route, pause here
    finally:
        db.close()        # 3. when the route finishes, close it

