from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings, loading from environment variables or defaults."""
    CAT_FACT_API_URL: str = "https://catfact.ninja/fact"

settings = Settings()