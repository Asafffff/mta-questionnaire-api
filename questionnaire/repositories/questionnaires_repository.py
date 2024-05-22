from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from questionnaire.repositories.mongo_repository import get_database
from questionnaire.repositories import BaseRepository


class QuestionnairesRepository(BaseRepository):
    def __init__(self, db: AsyncIOMotorDatabase = Depends(get_database)) -> None:
        self.collectionName = "questionnaires"
        super().__init__(db.get_collection(self.collectionName))
