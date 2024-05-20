from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from src.openapi_server.core.settings import settings
from typing import AsyncGenerator

client = AsyncIOMotorClient(settings.DATABASE_URL)
db = client[settings.DATABASE_NAME]


async def get_database() -> AsyncGenerator:
    yield db
