import datetime
from decimal import Decimal
from typing import Dict

from pydantic import BaseModel

from app.insurance.models import CargoTypes


class CalculateRequest(BaseModel):
    date: datetime.date
    cargo_type: CargoTypes
    declared_value: Decimal


class CalculateResponse(BaseModel):
    insurance_value: Decimal


class CurrentTariff(BaseModel):
    rate: str
    cargo_type: str


class CurrentTariffs(BaseModel):
    current_tariffs: Dict[str, CurrentTariff]


class Insurance(BaseModel):
    date: datetime.date
    cargo_type: CargoTypes
    rate: Decimal
