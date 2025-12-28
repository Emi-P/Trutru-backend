from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.deps import get_db
from models.match import Match, MatchStatus

router = APIRouter(prefix="/matches", tags=["matches"])


@router.post("/")
def create_game(db: Session = Depends(get_db)):
    match = Match(status=MatchStatus.waiting)

    db.add(match)
    db.commit()
    db.refresh(match)

    return {
        "match": match.id,
        "status": match.status,
    }
