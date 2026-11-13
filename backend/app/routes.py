from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from .database import get_db
from .models import Team

router = APIRouter(prefix="/api", tags=["api"])
DbSession = Annotated[Session, Depends(get_db)]


@router.get("/v1/health")
def health_check():
    return {"status": "ok"}


@router.get("/v1/team")
def get_team(db: DbSession):
    team = db.scalar(
        select(Team)
        .options(selectinload(Team.members))
        .where(Team.name == "sojáci")
    )
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")

    return {"name": team.name, "members": [member.name for member in team.members]}
