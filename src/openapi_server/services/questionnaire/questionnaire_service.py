from fastapi import Depends
from typing import List
from src.openapi_server.models.answer import Answer
from src.openapi_server.models.question import Question
from src.openapi_server.models.questionnaire_submission import QuestionnaireSubmission
from src.openapi_server.repositories.mongo_repository import get_database
import logging
from motor.motor_asyncio import AsyncIOMotorDatabase

logger = logging.getLogger(__name__)


class QuestionnaireService:
    def __init__(self, db: AsyncIOMotorDatabase = Depends(get_database)):
        self.db = db

    async def submit(
        self,
        questionnaire_submission: QuestionnaireSubmission,
    ) -> None:
        logger.info("Received questionnaire submission")
        logger.debug(questionnaire_submission)

        answersArray = []
        for answer in questionnaire_submission.answers:
            answersArray.append(
                Answer(
                    user_id="TEST",
                    question_id=answer.question_id,
                    answer=answer.text,
                ).model_dump()
            )

        result = await self.db["answers"].insert_many(answersArray)

        logger.info("Saved questionnaire submission")

        return

    async def get_questions(self, questionnaire_id: str) -> List[Question]:
        logger.info("Getting questions by given questionareId")
        cursor = self.db["questions"].find({"questionnaire_id": questionnaire_id})
        result = await cursor.to_list(length=200)
        logger.info(f"Found {len(result)} questions")

        serialized_result = [Question(**doc) for doc in result]

        return serialized_result
