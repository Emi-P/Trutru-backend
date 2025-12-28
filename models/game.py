from db.session import Base

from sqlalchemy import Integer, Boolean, String, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.orderinglist import ordering_list
from enum import IntEnum, Enum

class Partida(BaseModel):
    id: int
    status: Status 
    name: str
    PlayerAmount: PlayerAmount
    Gamestate: int

class Status(Enum):
    active = 'active'
    waiting = 'waiting'
    finished = 'finished'

class PlayerAmount(IntEnum):
     = 
