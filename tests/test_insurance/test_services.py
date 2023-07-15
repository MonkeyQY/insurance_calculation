import asyncio
from _decimal import Decimal
from datetime import datetime

import pytest

from app.database import database
from app.insurance.manager import get_insurance_manager, InsuranceManager
from app.insurance.schemas import CalculateRequest
from app.insurance.services import calculate_insurance, get_current_rate


@pytest.fixture(scope='session', autouse=True)
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
def database_connect():
    loop = asyncio.get_event_loop()
    yield loop.run_until_complete(database.connect())
    loop.run_until_complete(database.disconnect())


@pytest.fixture
def add_rate():
    loop = asyncio.get_event_loop()
    manager: InsuranceManager = get_insurance_manager()
    loop.run_until_complete(manager.add_rate_for_date_and_type(datetime.today(), "Other", Decimal("0.01")))


@pytest.fixture()
def delete_all() -> None:
    manager = get_insurance_manager()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(manager._InsuranceManager__delete_all())


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
@pytest.mark.usefixtures("database_connect", "delete_all", "add_rate")
@pytest.mark.parametrize(
    "data, insurance",
    [
        (CalculateRequest(date=datetime.today(), cargo_type="Other", declared_value=Decimal("1000")), Decimal("0.01")),
        (CalculateRequest(date=datetime.today(), cargo_type="Other", declared_value=Decimal("1000")), Decimal("0.01")),
        (CalculateRequest(date=datetime.today(), cargo_type="Other", declared_value=Decimal("1000")), Decimal("0.01")),
    ]
)
async def test_get_current_rate(data: CalculateRequest, insurance: Decimal):
    assert await get_current_rate(data) == insurance
