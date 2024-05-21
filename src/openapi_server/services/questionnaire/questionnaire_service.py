from fastapi import Depends
from typing import Annotated, List
from src.openapi_server.repositories import (
    QuestionnairesRepository,
    QuestionsRepository,
    AnswersRepository,
)
from src.openapi_server.models import (
    Question,
    Questionnaire,
    QuestionnaireSubmission,
    AnswerDB,
)

from src.openapi_server.repositories.mongo_repository import get_database
import logging
from motor.motor_asyncio import AsyncIOMotorDatabase

logger = logging.getLogger(__name__)


class QuestionnaireService:
    def __init__(
        self,
        questionnaireRepository: Annotated[
            AsyncIOMotorDatabase, Depends(QuestionnairesRepository)
        ],
        questionsRepository: Annotated[
            AsyncIOMotorDatabase, Depends(QuestionsRepository)
        ],
        answerRepository: Annotated[AsyncIOMotorDatabase, Depends(AnswersRepository)],
    ):
        self.questionnaireRepository = questionnaireRepository
        self.questionsRepository = questionsRepository
        self.answerRepository = answerRepository

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
                AnswerDB(
                    user_id=user_id,
                    question_id=answer.question_id,
                    text=answer.text,
                ).model_dump(by_alias=True)
            )

        await self.answerRepository.insert_many(answersArray)

        logger.info("Saved questionnaire submission")

        return

    async def get_questionnaires(self) -> List[Questionnaire]:
        logger.info("Getting all questionnaires")
        cursor = self.questionnaireRepository.find()
        result = await cursor.to_list(length=20)
        logger.info(f"Found {len(result)} questionnaires")

        serialized_result = [Questionnaire(**doc) for doc in result]

        return serialized_result

    async def get_questions(self, questionnaire_id: str) -> List[Question]:
        logger.info("Getting questions by given questionareId")
        cursor = self.questionsRepository.find({"questionnaire_id": questionnaire_id})
        result = await cursor.to_list(length=50)
        logger.info(f"Found {len(result)} questions")

        serialized_result = [Question(**doc) for doc in result]

        return serialized_result
