from typing import Annotated, Optional
from fastapi import Depends, FastAPI, Request, HTTPException
from fastapi.security import OAuth2PasswordBearer
from starlette.responses import Response
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import SecurityScopes, HTTPAuthorizationCredentials, HTTPBearer
from src.openapi_server.core.settings import settings

app = FastAPI()

SECRET_KEY = "t9FGxWZCb6rmXGIGpUYUUYxMkGdGRc0j"
ALGORITHM = "HS256"


class VerifyToken:
    """Does all the token verification using PyJWT"""

    def __init__(self):
        self.config = settings

        jwks_url = f"https://{self.config.AUTH_DOMAIN}/.well-known/jwks.json"
        self.jwks_client = jwt.PyJWKClient(jwks_url)

    async def verify(
        self,
        security_scopes: SecurityScopes,
        token: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer()),
    ):
        if token is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(
                token.credentials
            ).key
        except jwt.exceptions.PyJWKClientError as error:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail=str(error)
            )
        except jwt.exceptions.DecodeError as error:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail=str(error)
            )

        try:
            payload = jwt.decode(
                token.credentials,
                signing_key,
                algorithms=self.config.AUTH_ALGORITHMS,
                audience=self.config.AUTH_API_AUDIENCE,
                issuer=self.config.AUTH_ISSUER,
            )
        except Exception as error:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail=str(error)
            )

        return payload
