from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "AI Resume & Job Match Analyzer"
    mongodb_uri: str = "mongodb://localhost:27017"
    database_name: str = "resume_matcher"
    frontend_url: str = "http://localhost:5173"
    max_upload_size_mb: int = 10
    embedding_model: str = "all-MiniLM-L6-v2"
    openai_api_key: str = ""

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = Settings()
