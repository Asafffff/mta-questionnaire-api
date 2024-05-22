from fastapi import Depends
from typing import Annotated, List
from questionnaire.logger import logger
from motor.motor_asyncio import AsyncIOMotorDatabase
from questionnaire.repositories import QuestionsRepository
from questionnaire.models import Question


class QuestionsService:
    def __init__(
        self,
        questionsRepository: Annotated[
            AsyncIOMotorDatabase, Depends(QuestionsRepository)
        ],
    ):
        self.questionsRepository = questionsRepository

    async def get_questions(self, questionnaire_id: str) -> List[Question]:
        logger.info("Getting questions by given questionareId")
        cursor = self.questionsRepository.find({"questionnaire_id": questionnaire_id})
        result = await cursor.to_list(length=50)
        logger.info(f"Found {len(result)} questions")

        serialized_result = [Question(**doc) for doc in result]

        return serialized_result
