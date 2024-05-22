from motor.motor_asyncio import AsyncIOMotorClient
from questionnaire.core import settings


class MongoDBClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(MongoDBClient, cls).__new__(cls, *args, **kwargs)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.client = AsyncIOMotorClient(settings.DATABASE_URL)
        self.db = self.client[settings.DATABASE_NAME]

    def get_collection(self, collection_name):
        return self.db[collection_name]


def get_database():
    return MongoDBClient()
