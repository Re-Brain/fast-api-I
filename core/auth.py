from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import os
from dotenv import load_dotenv

load_dotenv()

# The "password" only your server knows — used to sign and verify tokens. Keep this secret.
SECRET_KEY = os.getenv("SECRET_KEY")

# The signing method (not secret, just a specification). HS256 = HMAC with SHA-256.
# SECRET_KEY is *what* signs the token, ALGORITHM is *how* the signing math is done.
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def hash_password(password: str) -> str:

    # Hash the password using bcrypt
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:

    # Verify the password against the hashed version
    # The plain password is hashed and compared to the stored hash
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict) -> str:

    # Create a JWT token with an expiration time
    to_encode = data.copy() # Pass by reference
    
    # Set the expiration time for the token
    # Use UTC timezone to avoid issues with daylight saving time and time zones
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode["exp"] = expire

    # to_encode = { "sub": user email, "exp": expiration_time }
    #
    # JWT has 3 parts separated by dots: header.payload.signature
    # - header    : metadata (algorithm used). Not secret, anyone can read it.
    # - payload   : your data (sub, exp). Not secret, anyone can decode it.
    # - signature : HMAC_SHA256(header + payload, SECRET_KEY). Only your server can verify it.
    #
    # JWT is NOT encrypted — it is SIGNED. Data is readable but cannot be tampered with.
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str = Depends(oauth2_scheme)):

    # Create an exception to raise if token is invalid
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:

        # Decode the token and extract the email (subject)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        
        # If email is missing, the token is invalid
        if email is None:
            raise credentials_exception
        
        # Return the email (or you could return a user object or other data as needed)
        return email
    
    except JWTError:

        # If any error occurs during decoding (invalid token, expired, wrong signature), raise the credentials exception
        raise credentials_exception
