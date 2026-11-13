from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from .config import settings


class Base(DeclarativeBase):
    pass


engine = create_engine(settings.database_url, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def initialize_database():
    from .models import Team, TeamMember

    Base.metadata.create_all(bind=engine)

    with SessionLocal() as db:
        team = db.scalar(select(Team).where(Team.name == "sojáci"))
        if team is None:
            team = Team(name="sojáci")
            db.add(team)
            db.flush()

        existing_members = {member.name for member in team.members}
        for name in ("Max", "Maxim", "Patrick"):
            if name not in existing_members:
                team.members.append(TeamMember(name=name))

        db.commit()
