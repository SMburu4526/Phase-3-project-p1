from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Locker(Base):
    __tablename__ = "lockers"

    id = Column(Integer, primary_key=True)
    player_name = Column(String, nullable=False)
    sport = Column(String, nullable=False)
    equipment = Column(String)
    team_id = Column(Integer, ForeignKey("teams.id"))

    team = relationship("Team", back_populates="lockers")

    def __repr__(self):
        return f"<Locker {self.id}: {self.player_name} ({self.sport}) - {self.equipment}>"
