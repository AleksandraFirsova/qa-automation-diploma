import allure
from selene import browser

from config.ui_config import UIConfig


class BasePage:
    url: str = ""

    def open(self):
        full_url = UIConfig.BASE_URL + self.url

        with allure.step(f"Открытие страницы: {full_url}"):
            browser.open(full_url)
