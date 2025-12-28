# app/models/partida.py

from sqlalchemy import Column, Integer, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

from db.base import Base


class MatchStatus(enum.Enum):
    waiting = "waiting"
    active = "active"
    finished = "finished"


class Match(Base):
    __tablename__ = "matches"

    id = Column(Integer, primary_key=True, index=True)

    status = Column(Enum(MatchStatus), nullable=False)

    created_at = Column(DateTime, default=datetime.now)
    finished_at = Column(DateTime, nullable=True)

    score_team_1 = Column(Integer, default=0)
    score_team_2 = Column(Integer, default=0)

    winner_team = Column(Integer, nullable=True)

    mode = Column(Integer, default=2) # Amount of players 2, 4 ,6

