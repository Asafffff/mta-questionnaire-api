from fastapi import (
    APIRouter,
    Depends,
    Query,
)
from questionnaire.auth.auth_strategy import authStrategy
from questionnaire.services import QuestionsService
from questionnaire.models import APIResponse

router = APIRouter()


@router.get(
    "/",
    dependencies=[Depends(authStrategy.verify)],
    responses={
        200: {"model": APIResponse, "description": "A list of questions"},
        400: {"description": "Invalid parameter"},
        500: {"description": "Internal server error"},
    },
    tags=["default"],
    summary="Get all questions",
    response_model_by_alias=True,
)
async def questions_get(
    questionnaire_id: str = Query(
        description="ID of the questionnaire to filter questions",
        alias="questionnaire_id",
    ),
    service: QuestionsService = Depends(QuestionsService),
) -> APIResponse:
    """Retrieve all questions, optionally filtered by questionnaire_id"""

    result = await service.get_questions(questionnaire_id)

    return APIResponse(data=result)
