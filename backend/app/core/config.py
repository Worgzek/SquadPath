from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 10080
    GEMINI_API_KEY: str
    LLM_PROVIDER: str = "gemini"

    class Config:
        env_file = ".env"

settings = Settings()