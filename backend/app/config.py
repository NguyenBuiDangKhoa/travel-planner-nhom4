import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Multi-Agent AI Travel Planner"
    API_V1_STR: str = "/api"
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    
    # Defaults
    DEFAULT_MODEL: str = "gemini-flash-latest"  # Sử dụng gemini-flash-latest để có hạn mức Free Tier cao và tránh lỗi 404 v1beta

settings = Settings()
