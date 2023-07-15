from _decimal import Decimal
from datetime import datetime
from unittest.mock import AsyncMock

import pytest

from app.insurance.schemas import CalculateRequest
from app.insurance.services import calculate_insurance, get_current_rate


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "declared_value, rate, expected",
    [
        (Decimal("1000"), Decimal("0.01"), Decimal("10")),
        (Decimal("1000"), Decimal("0.02"), Decimal("20")),
        (Decimal("1000"), Decimal("0.03"), Decimal("30")),
        (Decimal("1000"), Decimal("0.04"), Decimal("40")),
    ]
)
async def test_calculate_insurance(declared_value: Decimal, rate: Decimal, expected: Decimal):
    assert await calculate_insurance(declared_value, rate) == expected


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "data, insurance",
    [
        (CalculateRequest(date=datetime.today(), cargo_type="Other", declared_value=Decimal("1000")), Decimal("0.01")),
        (CalculateRequest(date=datetime.today(), cargo_type="Other", declared_value=Decimal("1000")), Decimal("0.01")),
        (CalculateRequest(date=datetime.today(), cargo_type="Other", declared_value=Decimal("1000")), Decimal("0.01")),
    ]
)
async def test_get_current_rate(data: CalculateRequest, insurance: Decimal):
    mock_manager = AsyncMock()
    mock_manager.get_rate_for_date_and_type.return_value = insurance
    assert await get_current_rate(data, mock_manager) == insurance
