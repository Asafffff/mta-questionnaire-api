# Questionnaire API

## Description

This project provides an API for submitting questionnaires with an array of answers. It includes endpoints for managing questionnaires and their questions.

## Prerequisites

- Python 3.9+

### .env File properties:

Create a `.env` file in the root directory of the project with the following properties:

### .env File properties:

```.env
DATABASE_URL=<MONGODB_DB_URL>
DATABASE_NAME=<MONGODB_DB_NAME>

AUTH_DOMAIN=<STRING>
AUTH_API_AUDIENCE=<STRING>
AUTH_ISSUER=<STRING>
AUTH_ALGORITHMS=RS256

```

## Installation

Clone the repository and navigate to the project directory
Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

# Usage

FastAPI

To use the script as part of a FastAPI application, you can start the server with Uvicorn. Ensure you are in the root directory of your project, and then run:

```bash
make run
```

This will serve the FastAPI application where you can access the API endpoint to fetch approval events.
