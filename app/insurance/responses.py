from app.insurance.exceptions import RateNotFound

insurance_responses = {
    400: {
        "model": RateNotFound,
        "description": "Rate not found",
    }
}
