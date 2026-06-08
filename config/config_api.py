import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_URL = os.getenv("BASE_URL")

    USERNAME = os.getenv("BOOKER_USERNAME")
    PASSWORD = os.getenv("BOOKER_PASSWORD")
