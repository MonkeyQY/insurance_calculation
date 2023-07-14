from _decimal import Decimal
from datetime import datetime

from aiohttp import ClientSession

from app import config
from app.insurance.manager import InsuranceManager, get_insurance_manager
from app.insurance.schemas import CurrentTariffs


async def get_current_tariffs() -> None:
    async with ClientSession() as client:
        async with client.get(config.current_tariffs_url) as response:
            data = CurrentTariffs(current_tariffs=await response.json())
            await save_current_tariffs(data)


async def save_current_tariffs(
    tariffs: CurrentTariffs, manager: InsuranceManager = get_insurance_manager()
) -> None:
    for date, value in tariffs.current_tariffs.items():
        rate = await manager.get_rate_for_date_and_type(
            datetime.strptime(date, "%Y-%m-%d"), value.cargo_type
        )
        if rate is not None:
            await manager.update_insurance(
                datetime.strptime(date, "%Y-%m-%d"),
                value.cargo_type,
                Decimal(value=value.rate),
            )
        else:
            await manager.add_rate_for_date_and_type(
                datetime.strptime(date, "%Y-%m-%d"),
                value.cargo_type,
                Decimal(value=value.rate),
            )
