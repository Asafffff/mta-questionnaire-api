# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from src.openapi_server.models.api_response import APIResponse
import src.openapi_server.services

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    HTTPException,
    Header,
    Path,
    Query,
    Response,
    Security,
    status,
)

from src.openapi_server.services.questionnaire.questionnaire_service import (
    QuestionnaireService,
)
from src.openapi_server.models.extra_models import TokenModel  # noqa: F401
from src.openapi_server.models.error_response import ErrorResponse
from src.openapi_server.models.questionnaire_submission import QuestionnaireSubmission


router = APIRouter()

ns_pkg = src.openapi_server.services
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/questionnaire",
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
    service: QuestionnaireService = Depends(QuestionnaireService),
) -> APIResponse:
    await service.submit(questionnaire_submission)
    return APIResponse(data="Questionnaire submitted successfully")


@router.get(
    "/questions",
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
        None,
        description="ID of the questionnaire to filter questions",
        alias="questionnaire_id",
    ),
    service: QuestionnaireService = Depends(QuestionnaireService),
) -> APIResponse:
    """Retrieve all questions, optionally filtered by questionnaire_id"""
    if not questionnaire_id:
        raise HTTPException(
            400, detail=f"Missing required parameter 'questionnaire_id'"
        )
    result = await service.get_questions(questionnaire_id)

    return APIResponse(data=result)