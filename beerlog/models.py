from datetime import datetime
from statistics import mean
from typing import Optional

from pydantic import validator
from sqlmodel import Field, SQLModel


class Beer(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, default=None, index=True)
    name: str
    style: str
    flavor: int
    image: int
    cost: int
    rate: int = 0
    date: datetime = Field(default_factory=datetime.now)

    @validator("flavor", "image", "cost")
    def validate_ratings(cls, value, field):
        if value < 1 or value > 10:
            raise RuntimeError(f"{field.name} must be between 1 and 10")
        return value

    @validator("rate", always=True)
    def cauculate_rate(cls, value, values):
        return int(mean([values["flavor"], values["image"], values["cost"]]))
