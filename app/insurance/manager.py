from _decimal import Decimal
import datetime
from typing import Optional, Any

from databases import Database
from databases.interfaces import Record

from app.database import database
from app.insurance.models import insurance
from app.insurance.schemas import Insurance


# мэнеджер для черепахи
# class InsuranceManager:
#     def __init__(self, database: Insurance):
#         self.database = database
#
#     async def add_rate_for_date_and_type(
#         self, date: datetime.date, cargo_type: str, rate: Decimal
#     ):
#         return await self.database.create(date=date, cargo_type=cargo_type, rate=rate)
#
#     async def get_rate_for_date_and_type(
#         self, date: datetime.date, cargo_type: str
#     ) -> Optional[Decimal]:
#         return await self.database.get_or_none(date=date, cargo_type=cargo_type).only(
#             "rate"
#         )


class InsuranceManager:
    def __init__(self, database: Database):
        self.database = database

    async def add_rate_for_date_and_type(
        self, date: datetime.date, cargo_type: str, rate: Decimal
    ) -> Any:
        query = insurance.insert().values(date=date, cargo_type=cargo_type, rate=rate)
        return await self.database.execute(query=query)

    async def get_rate_for_date_and_type(
        self, date: datetime.date, cargo_type: str
    ) -> Optional[Decimal]:
        query = insurance.select().where(
            insurance.c.date == date, insurance.c.cargo_type == cargo_type
        )
        record: Optional[Record] = await self.database.fetch_one(query=query)

        if record is None:
            return None

        return Insurance.parse_obj(record).rate

    async def update_insurance(
        self, date: datetime.date, cargo_type: str, rate: Decimal
    ) -> None:
        query = (
            insurance.update()
            .where(insurance.c.date == date, insurance.c.cargo_type == cargo_type)
            .values(rate=rate)
        )
        await self.database.execute(query=query)
        return

    async def __delete_all(self):
        query = insurance.delete()
        await self.database.execute(query=query)
        return


def get_insurance_manager() -> InsuranceManager:
    return InsuranceManager(database)
