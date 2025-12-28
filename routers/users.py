from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.deps import get_db
from models.match import Match, MatchStatus

router = APIRouter(prefix="/users", tags=["users"])
