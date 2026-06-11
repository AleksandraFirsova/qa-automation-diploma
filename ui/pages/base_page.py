import allure
from selene import browser


class BasePage:
    def open(self, url: str):
        with allure.step(f"Открытие страницы: {url}"):
            browser.open(url)
