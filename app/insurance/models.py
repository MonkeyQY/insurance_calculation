from enum import Enum

from sqlalchemy import Table, Column, Date, DECIMAL, Enum as CharEnumField

from app.database import metadata


class CargoTypes(str, Enum):
    glass = "Glass"
    other = "Other"


# Т.к. черепаха не поддерживает 2 primary key, то пришлось перейти
# на sqlAlchemy, черепашку можно выкинуть)
# class Insurance(Model):
#     date = fields.DateField(pk=True)
#     cargo_type = fields.CharEnumField(CargoTypes, max_length=50, pk=True)
#     rate = fields.DecimalField(18, 5)


insurance = Table(
    "insurance",
    metadata,
    Column("date", Date, primary_key=True),
    Column("cargo_type", CharEnumField(CargoTypes), primary_key=True),
    Column("rate", DECIMAL(18, 5)),
)
