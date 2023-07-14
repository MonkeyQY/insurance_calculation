from databases import Database
from sqlalchemy import MetaData, create_engine

from sqlalchemy.engine import URL

from app import config

# SQLAlchemy интереснее черепашки)
database_url = URL.create(**config.DATABASE)
database = Database(str(database_url))
engine = create_engine(database_url)

metadata = MetaData()


# async def init_db():
#     await Tortoise.init(
#         db_url=str(database_url), modules={"models": ["app.insurance.models"]}
#     )
#     await Tortoise.generate_schemas()
#
#
# async def shutdown_db():
#     await Tortoise.close_connections()
