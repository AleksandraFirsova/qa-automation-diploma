import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env.ui", override=True)


class UIConfig:
    BASE_URL = os.getenv("BASE_URL")

    BROWSER = os.getenv("BROWSER", "chrome")

    BROWSER_VERSION = os.getenv("BROWSER_VERSION", "127.0")

    SELENOID_URL = os.getenv("SELENOID_URL")

    SCREEN_WIDTH = int(os.getenv("SCREEN_WIDTH", "1920"))
    SCREEN_HEIGHT = int(os.getenv("SCREEN_HEIGHT", "1080"))

    HEADLESS = os.getenv("HEADLESS", "true").lower() == "true"
