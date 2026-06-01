from sqlalchemy import Column, Integer, String
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
