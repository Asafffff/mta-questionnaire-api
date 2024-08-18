from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )
    DATABASE_URL: str
    DATABASE_NAME: str

    FIREBASE_AUTH_SERVICE_ACCOUNT_BASE64_STRING: str


settings = Settings()
