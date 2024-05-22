from fastapi import Depends
from typing import Annotated, List
from questionnaire.logger import logger
from motor.motor_asyncio import AsyncIOMotorDatabase
from questionnaire.repositories import QuestionnairesRepository, AnswersRepository
from questionnaire.models import Questionnaire, QuestionnaireSubmission, AnswerDB


class QuestionnairesService:
    def __init__(
        self,
        questionnairesRepository: Annotated[
            AsyncIOMotorDatabase, Depends(QuestionnairesRepository)
        ],
        answerRepository: Annotated[AsyncIOMotorDatabase, Depends(AnswersRepository)],
    ):
        self.questionnairesRepository = questionnairesRepository
        self.answerRepository = answerRepository

    async def get_questionnaires(self) -> List[Questionnaire]:
        logger.info("Getting all questionnaires")
        cursor = self.questionnairesRepository.find()
        result = await cursor.to_list(length=20)
        logger.info(f"Found {len(result)} questionnaires")

        serialized_result = [Questionnaire(**doc) for doc in result]

        return serialized_result

    async def submit_answers(
        self,
        questionnaire_submission: QuestionnaireSubmission,
        user_id: str,
    ) -> None:
        logger.info("Received questionnaire submission")
        logger.debug(questionnaire_submission)

        answersArray = [
            AnswerDB(
                user_id=user_id,
                question_id=answer.question_id,
                text=answer.text,
            ).model_dump(by_alias=True)
            for answer in questionnaire_submission.answers
        ]

        await self.answerRepository.insert_many(answersArray)

        logger.info("Saved questionnaire submission")

        return
