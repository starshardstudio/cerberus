import sqlalchemy
import sqlalchemy.orm 

from ..config import DATABASE_URL


engine = sqlalchemy.create_engine(url=DATABASE_URL)
Session = sqlalchemy.orm.sessionmaker(bind=engine)


__all__ = (
    "engine",
    "Session",
)
