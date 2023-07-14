from pydantic import BaseModel


class RateNotFound(BaseModel):
    detail: str = "Rate not found"
