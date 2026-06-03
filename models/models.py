from sqlalchemy import Column, Integer, String, Boolean
from database import Base

class Horse(Base):
    __tablename__ = "horses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    title = Column(String)
    img = Column(String)
    age = Column(Integer)
    record = Column(String)
    trainer = Column(String)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="visitor")  # visitor | farmer | admin
    phone_code = Column(String, nullable=True)   # e.g. +1, +44, +66
    phone_number = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)



