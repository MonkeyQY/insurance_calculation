from fastapi import APIRouter

from app.insurance.responses import insurance_responses
from app.insurance.schemas import CalculateResponse, CalculateRequest
from app.insurance.services import calculate_insurance


router = APIRouter()


@router.post(
    "/calculate/", response_model=CalculateResponse, responses=insurance_responses
)
async def calculate(data: CalculateRequest) -> CalculateResponse:
    """Calculates insurance value"""
    insurance_value = await calculate_insurance(data)
    return CalculateResponse(insurance_value=insurance_value)
