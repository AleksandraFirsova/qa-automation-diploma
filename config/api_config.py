import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env.api", override=True)


class ApiConfig:
    BASE_URL = os.getenv("BASE_URL")

    USERNAME = os.getenv("BOOKER_USERNAME")
    PASSWORD = os.getenv("BOOKER_PASSWORD")
