from fastapi import FastAPI
import logging
import os
import json
import base64
import firebase_admin
from firebase_admin import credentials
from questionnaire.core import settings

from .router import main_router as DefaultApiRouter

logging.basicConfig(level=logging.DEBUG)

app = FastAPI(
    title="Questionnaire API",
    description="API for submitting sleep, mood, and diet questionnaires",
    version="1.0.0",
)

app.include_router(DefaultApiRouter)

decoded_credentials = base64.b64decode(
    settings.FIREBASE_AUTH_SERVICE_ACCOUNT_BASE64_STRING
).decode("utf-8")
service_account_info = json.loads(decoded_credentials)

cred = credentials.Certificate(service_account_info)
firebase_admin.initialize_app(cred)
