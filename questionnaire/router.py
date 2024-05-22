# router.py
from fastapi import APIRouter
from questionnaire.apis.questionnaire_controller import router as questionnaire_router
from questionnaire.apis.questions_controller import router as questions_router

main_router = APIRouter()

main_router.include_router(questionnaire_router, prefix="/questionnaires")
main_router.include_router(questions_router, prefix="/questions")
