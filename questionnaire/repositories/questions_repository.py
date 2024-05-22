from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from questionnaire.repositories.mongo_repository import get_database
from questionnaire.repositories import BaseRepository


class QuestionsRepository(BaseRepository):
    def __init__(self, db: AsyncIOMotorDatabase = Depends(get_database)) -> None:
        self.collectionName = "questions"
        super().__init__(db.get_collection(self.collectionName))
