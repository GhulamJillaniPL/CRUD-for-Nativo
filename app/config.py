from pydantic import BaseSettings

class Settings(BaseSettings):
    nativo_api_key: str
    nativo_api_secret: str
    database_url: str

    class Config:
        env_file = ".env"

settings = Settings()
