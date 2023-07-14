from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from sqlalchemy.engine import URL

from app import config
from app.database import engine
from app.insurance.getting_current_tariffs import current_tariffs

schedule = AsyncIOScheduler(
    job_defaults={
        "max_instances": 1,
        "coalesce": True,
        "misfire_grace_time": 3600,
    },
)

scheduler_job_store = SQLAlchemyJobStore(
    url=str(URL.create(**config.DATABASE)), engine=engine
)

schedule.add_jobstore(scheduler_job_store)

schedule.add_job(
    current_tariffs,
    trigger="cron",
    day_of_week="mon-sun",
    hour="20",
    minute="0",
    id="current_tariffs",
    replace_existing=True,
)
