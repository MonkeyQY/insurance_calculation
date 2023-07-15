from decimal import Decimal

from fastapi import HTTPException

from app.insurance.manager import get_insurance_manager, InsuranceManager
from app.insurance.schemas import CalculateRequest


async def get_insurance(data: CalculateRequest) -> Decimal:
    rate = await get_current_rate(data)
    insurance = await calculate_insurance(data.declared_value, rate)
    return insurance


async def calculate_insurance(declared_value: Decimal, rate: Decimal) -> Decimal:
    return declared_value * rate


async def get_current_rate(
        data: CalculateRequest, manager: InsuranceManager = get_insurance_manager()
) -> Decimal:
    rate = await manager.get_rate_for_date_and_type(data.date, data.cargo_type.name)
    if rate is None:
        raise HTTPException(status_code=404, detail="Rate not found")
    return rate
