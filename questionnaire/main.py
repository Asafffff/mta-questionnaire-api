from fastapi import FastAPI
import logging

from .router import main_router as DefaultApiRouter

logging.basicConfig(level=logging.DEBUG)

app = FastAPI(
    title="Questionnaire API",
    description="API for submitting sleep, mood, and diet questionnaires",
    version="1.0.0",
)

app.include_router(DefaultApiRouter)
