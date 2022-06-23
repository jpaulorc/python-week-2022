import warnings

from sqlalchemy.exc import SAWarning
from sqlmodel import Session, create_engine
from sqlmodel.sql.expression import Select, SelectOfScalar

from beerlog import models
from beerlog.config import settings

warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True  # type: ignore
Select.inherit_cache = True  # type: ignore

engine = create_engine(settings.database.url, echo=False)
models.SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
