from fastapi import (
    APIRouter,
    Body,
    Depends,
    Security,
)
from questionnaire.auth.auth_strategy import authStrategy
from questionnaire.services import QuestionnairesService
from questionnaire.models import APIResponse, ErrorResponse, QuestionnaireSubmission

router = APIRouter()


@router.get(
    "/",
    dependencies=[Depends(authStrategy)],
    responses={
        200: {"model": APIResponse, "description": "A list of questionnaires"},
        500: {"description": "Internal server error"},
    },
    tags=["default"],
    summary="Get all questionnaires",
    response_model_by_alias=True,
)
async def questionnaires_get(
    service: QuestionnairesService = Depends(QuestionnairesService),
) -> APIResponse:
    """Retrieve all questionnaires"""

    result = await service.get_questionnaires()

    return APIResponse(data=result)


@router.post(
    "/",
    dependencies=[Depends(authStrategy)],
    responses={
        200: {
            "model": APIResponse,
            "description": "Questionnaire submitted successfully",
        },
        400: {"model": ErrorResponse, "description": "Invalid input data"},
        401: {"model": ErrorResponse, "description": "Authentication required"},
        500: {"model": ErrorResponse, "description": "Internal server error"},
    },
    tags=["default"],
    summary="Submit Questionnaire",
    response_model_by_alias=True,
)
async def questionnaire_post(
    questionnaire_submission: QuestionnaireSubmission = Body(None, description=""),
    auth_result: dict = Security(authStrategy),
    service: QuestionnairesService = Depends(QuestionnairesService),
) -> APIResponse:
    """Submit a questionnaire"""

    await service.submit_answers(questionnaire_submission, user_id=auth_result["sub"])

    return APIResponse(data="Questionnaire submitted successfully")
