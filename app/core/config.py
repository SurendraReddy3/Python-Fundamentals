from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = "Smart Parking Finder"
    mongodb_uri: str = Field(default="mongodb://localhost:27017")
    mongodb_db: str = Field(default="smart_parking")
    jwt_secret_key: str = Field(default="change-me-in-prod")
    jwt_algorithm: str = Field(default="HS256")
    access_token_expire_minutes: int = Field(default=60 * 12)
    admin_email: str | None = Field(default=None)
    admin_password: str | None = Field(default=None)

    # pydantic-settings v2 config
    model_config = SettingsConfigDict(env_file=".env", env_prefix="", case_sensitive=False)

settings = Settings()
