from fastapi import APIRouter, HTTPException, status
from pymongo.errors import DuplicateKeyError
from typing import List

from src.openapi_server.models.user import User
from app.database import db

router = APIRouter()


@router.post("/", response_model=User)
async def create_user(user: User):
    try:
        user_dict = user.dict(by_alias=True)
        user_dict.pop("id", None)
        result = db["Users"].insert_one(user_dict)
        user_dict["_id"] = result.inserted_id
        return user_dict
    except DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists"
        )


@router.get("/{user_id}", response_model=User)
async def read_user(user_id: str):
    user = db["Users"].find_one({"_id": ObjectId(user_id)})
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return user
