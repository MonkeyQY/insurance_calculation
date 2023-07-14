import logging

import uvicorn
from fastapi import FastAPI

from app import config
from app.database import database
from app.insurance.routes import router as insurance_router
from app.scheduler.schedule import schedule

app = FastAPI(
    title="Insurance Calculate Service",
    description="Description",
    version="1.0.0",
    openapi_url=config.openapi_url,
    docs_url=config.docs_url,
    redoc_url=config.redoc,
)

logging.basicConfig(
    format="{asctime} : {levelname} : {name} : {message}",
    style="{",
    level=logging.INFO,
)

log: logging.Logger = logging.getLogger("main")


app.include_router(insurance_router, prefix="/insurance", tags=["insurances"])


@app.on_event("startup")
async def startup_event() -> None:
    await database.connect()
    schedule.start()


@app.on_event("shutdown")
async def shutdown_event() -> None:
    await database.disconnect()
    schedule.shutdown()


if __name__ == "__main__":
    uvicorn.run(
        "__main__:app",
        host=config.host,
        port=config.port,
        reload=config.reload,
        log_config=None,
    )
