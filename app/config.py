import os

from dotenv import load_dotenv

load_dotenv()

DATABASE = {
    "drivername": "postgresql+psycopg2",
    "host": os.environ.get("DB_HOST", "localhost"),
    "port": os.environ.get("DB_PORT", "5432"),
    "username": os.environ.get("DB_USER", "postgres"),
    "password": os.environ.get("DB_PASS", "postgres"),
    "database": os.environ.get("POSTGRES_DB", "insurance_calculate-db"),
}

openapi_url = os.getenv("OPENAPI_URL", "/openapi.json")
docs_url = os.getenv("DOCS_URL", "/docs")
host = os.getenv("HOST", "localhost")
port = int(os.getenv("PORT", 8080))
redoc = os.getenv("REDOC", "/redoc")

reload = os.getenv("RELOAD", "True") == "True"

current_tariffs_url = os.getenv(
    "CURRENT_TARIFFS_URL", "http://localhost:8080/current_tariffs"
)
