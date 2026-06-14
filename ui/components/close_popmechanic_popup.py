import allure
from selene import browser, be


class PopmechanicPopup:
    def close_popmechanic_popup(self):
        with allure.step("Проверка и закрытие popmechanic popup"):
            popup = browser.element('.popmechanic-main')

            if popup.matching(be.visible):
                with allure.step("Попап отображается, ищем кнопку закрытия"):
                    close_button = (
                        browser.all('.popmechanic-close')
                        .filtered_by(be.visible)
                        .first
                    )

                with allure.step("Закрываем попап"):
                    close_button.click()

                with allure.step("Проверяем, что попап закрыт"):
                    popup.should(be.not_.visible)
