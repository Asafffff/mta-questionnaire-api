from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )
    DATABASE_URL: str
    DATABASE_NAME: str

    AUTH_DOMAIN: str
    AUTH_API_AUDIENCE: str
    AUTH_ISSUER: str
    AUTH_ALGORITHMS: str


settings = Settings()
