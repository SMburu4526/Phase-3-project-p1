from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    lockers = relationship("Locker", back_populates="team", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Team {self.id}: {self.name}>"
