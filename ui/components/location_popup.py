import allure
from selene import browser, be


class LocationPopup:
    accept_button = browser.element(
        ".app-location-city-approve__button-accept"
    )

    def accept_city(self):
        with allure.step("Подтверждение выбора города в попапе"):
            if self.accept_button.matching(be.visible):
                with allure.step("Кнопка подтверждения видима — нажимаем"):
                    self.accept_button.click()
