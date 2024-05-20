# coding: utf-8

from fastapi.testclient import TestClient


from src.openapi_server.models.diet_questionnaire import DietQuestionnaire  # noqa: F401
from src.openapi_server.models.error_response import ErrorResponse  # noqa: F401
from src.openapi_server.models.mood_questionnaire import MoodQuestionnaire  # noqa: F401
from src.openapi_server.models.sleep_questionnaire import (
    SleepQuestionnaire,
)  # noqa: F401
from src.openapi_server.models.success_response import SuccessResponse  # noqa: F401


def test_questionnaire_diet_post(client: TestClient):
    """Test case for questionnaire_diet_post

    Submit Diet Questionnaire
    """
    diet_questionnaire = {
        "meal_category": "Vegetarian",
        "first_meal_time": "2000-01-23T04:56:07.000+00:00",
        "last_meal_time": "2000-01-23T04:56:07.000+00:00",
        "meal_description": "meal_description",
    }

    headers = {}
    # uncomment below to make a request
    # response = client.request(
    #    "POST",
    #    "/questionnaire/diet",
    #    headers=headers,
    #    json=diet_questionnaire,
    # )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_questionnaire_mood_post(client: TestClient):
    """Test case for questionnaire_mood_post

    Submit Mood Questionnaire
    """
    mood_questionnaire = {"mood_rating": 1}

    headers = {}
    # uncomment below to make a request
    # response = client.request(
    #    "POST",
    #    "/questionnaire/mood",
    #    headers=headers,
    #    json=mood_questionnaire,
    # )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200


def test_questionnaire_sleep_post(client: TestClient):
    """Test case for questionnaire_sleep_post

    Submit Sleep Questionnaire
    """
    sleep_questionnaire = {
        "sleep_end": "2000-01-23T04:56:07.000+00:00",
        "sleep_start": "2000-01-23T04:56:07.000+00:00",
        "sleep_quality": 1,
    }

    headers = {}
    # uncomment below to make a request
    # response = client.request(
    #    "POST",
    #    "/questionnaire/sleep",
    #    headers=headers,
    #    json=sleep_questionnaire,
    # )

    # uncomment below to assert the status code of the HTTP response
    # assert response.status_code == 200
