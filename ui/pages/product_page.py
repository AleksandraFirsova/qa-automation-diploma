import allure
from selene import browser, have, be

from ui.components.close_popmechanic_popup import PopmechanicPopup
from ui.pages.base_page import BasePage


class ProductPage(BasePage):

    def __init__(self):
        self.close_popmechanic_popup = PopmechanicPopup()

    @property
    def title(self):
        return browser.element('.product-title-author__title')

    @property
    def price(self):
        return browser.element('.price-block-price-info__price')

    @property
    def buy_button(self):
        return browser.all('button').element_by(
            have.text("Купить")
        )

    @property
    def checkout_button(self):
        return browser.all('button').element_by(
            have.text("Оформить")
        )

    @property
    def images(self):
        return browser.all('.product-preview__big-img')

    @property
    def reviews(self):
        return browser.all('.review')

    def add_to_cart(self):
        with allure.step("Добавление товара в корзину"):
            with allure.step("Нажатие кнопки 'Купить'"):
                self.buy_button.should(be.visible).click()

            with allure.step("Ожидание изменения состояния кнопки 'Купить'"):
                self.buy_button.with_(timeout=20).should(have.no.text("Купить"))

            with allure.step("Появление кнопки 'Оформить'"):
                self.checkout_button.with_(timeout=20).should(be.visible)

    def should_be_added(self):
        with allure.step("Проверка, что товар добавлен в корзину"):
            self.checkout_button.should(be.visible)
