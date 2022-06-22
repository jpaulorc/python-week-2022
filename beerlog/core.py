from typing import List, Optional

from sqlmodel import select

from beerlog.database import get_session
from beerlog.models import Beer
