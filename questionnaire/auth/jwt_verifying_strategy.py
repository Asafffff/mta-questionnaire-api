import jwt
from fastapi import Depends, HTTPException, Header
from fastapi.security import HTTPBearer
from firebase_admin import auth
from firebase_admin._auth_utils import InvalidIdTokenError
from questionnaire.logger import logger

bearer_scheme = HTTPBearer(auto_error=False)


async def firebase_verify_token(authorization: str = Header(...)):
    try:
        if not authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Invalid token header format")

        token = authorization[len("Bearer ") :]
        # Decode the JWT without verifying the signature
        decoded_token = jwt.decode(token, options={"verify_signature": False})
        return decoded_token
    except jwt.DecodeError:
        print("Failed to decode JWT.")
        return None

    # try:
    #     if not authorization.startswith("Bearer "):
    #         raise HTTPException(status_code=401, detail="Invalid token header format")

    #     token = authorization[len("Bearer ") :]

    #     decoded_token = auth.verify_id_token(token)
    #     return decoded_token
    # except InvalidIdTokenError as e:
    #     logger.error("Authentication error: %s", e)
    #     raise HTTPException(status_code=401, detail="Invalid token")
    # except Exception as e:
    #     # Handle other potential errors
    #     logger.error("Authentication error: %s", e)
    #     raise HTTPException(status_code=500, detail="Could not verify token")
