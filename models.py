from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

DATABASE_URL = "sqlite:///sports_locker.db"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
Base = declarative_base()

class Team(Base):
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)

    lockers = relationship("Locker", back_populates="team", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Team {self.id}: {self.name}>"

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
