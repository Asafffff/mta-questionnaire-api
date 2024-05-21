from fastapi import Depends
from typing import List
from src.openapi_server.models.questionnaire import Questionnaire
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

    async def submit_answers(
        self,
        questionnaire_submission: QuestionnaireSubmission,
        user_id: str,
    ) -> None:
        logger.info("Received questionnaire submission")
        logger.debug(questionnaire_submission)

        answersArray = []
        for answer in questionnaire_submission.answers:
            answersArray.append(
                Answer(
                    user_id=user_id,
                    question_id=answer.question_id,
                    answer=answer.text,
                ).model_dump(by_alias=True)
            )

        result = await self.db["answers"].insert_many(answersArray)

        logger.info("Saved questionnaire submission")

        return

    async def get_questionnaires(self) -> List[Questionnaire]:
        logger.info("Getting all questionnaires")
        cursor = self.db["questionnaires"].find()
        result = await cursor.to_list(length=20)
        logger.info(f"Found {len(result)} questionnaires")

        serialized_result = [Questionnaire(**doc) for doc in result]

        return serialized_result

    async def get_questions(self, questionnaire_id: str) -> List[Question]:
        logger.info("Getting questions by given questionareId")
        cursor = self.db["questions"].find({"questionnaire_id": questionnaire_id})
        result = await cursor.to_list(length=50)
        logger.info(f"Found {len(result)} questions")

        serialized_result = [Question(**doc) for doc in result]

        return serialized_result
