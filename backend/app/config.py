import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "Multi-Agent AI Travel Planner"
    API_V1_STR: str = "/api"
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    
    # Defaults
    DEFAULT_MODEL: str = "gemini-1.5-flash"  # Sử dụng 1.5-flash để có hạn mức Free Tier cao hơn (15 RPM / 1500 RPD)

settings = Settings()
