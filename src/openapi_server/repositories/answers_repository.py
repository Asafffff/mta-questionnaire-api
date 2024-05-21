from fastapi import Depends
from src.openapi_server.models.answer_db import AnswerDB
from src.openapi_server.repositories.base_repository import BaseRepository
from src.openapi_server.repositories.mongo_repository import get_database
from motor.motor_asyncio import AsyncIOMotorDatabase


class AnswersRepository(BaseRepository):
    def __init__(self, db: AsyncIOMotorDatabase = Depends(get_database)) -> None:
        self.collectionName = "answers"
        super().__init__(db.get_collection(self.collectionName))
