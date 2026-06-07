from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base

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

    farm = relationship("Farm", back_populates="owner", uselist=False, cascade="all, delete-orphan")


class Farm(Base):
    __tablename__ = "farms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=True)
    description = Column(Text, nullable=True)
    capacity = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=True)
    
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    owner = relationship("User", back_populates="farm", passive_deletes=True)

    horses = relationship("Horse", back_populates="farm")


class Horse(Base):
    __tablename__ = "horses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    title = Column(String, nullable=True)
    img = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    record = Column(String, nullable=True)
    trainer = Column(String, nullable=True)
    coat = Column(String, nullable=True)

    farm_id = Column(Integer, ForeignKey("farms.id"), nullable=True)
    farm = relationship("Farm", back_populates="horses")



