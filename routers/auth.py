from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import get_db
import models.models as models, schemas.auth as auth
from core.auth import hash_password, verify_password, create_access_token

router = APIRouter()

# 1 - API Route
# 2 - The shape of the response (schemas)
@router.post("/register", response_model=auth.Token)
def register(user: auth.UserCreate, db: Session = Depends(get_db)):

    # Cehck if user already exists
    existing = db.query(models.User).filter(models.User.email == user.email).first()
    
    # If user exists, raise an error
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # If not, create the user and return a token
    new_user = models.User(
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    
    # Add the user to the database and commit
    db.add(new_user)
    db.commit()
    
    # Refresh the instance to get the ID and other generated fields
    db.refresh(new_user)

    # Create a token for the new user using the email as the subject
    token = create_access_token({"sub": user.email})

    # token_type "bearer" = whoever holds this token is allowed in (like a concert ticket)
    return {"access_token": token, "token_type": "bearer"}

@router.post("/login", response_model=auth.Token)
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    # Find the user by email (username in form)
    user = db.query(models.User).filter(models.User.email == form.username).first()
    
    # If user not found or password doesn't match, raise an error
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Create a token for the user
    token = create_access_token({"sub": user.email})

    # token_type "bearer" = whoever holds this token is allowed in (like a concert ticket)
    return {"access_token": token, "token_type": "bearer"}
