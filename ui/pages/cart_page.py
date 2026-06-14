import allure
from selene import browser

from ui.pages.base_page import BasePage


class CartPage(BasePage):
    url = "/personal/cart"

    @property
    def items(self):
        return browser.all('.basket-item__card')

    @property
    def first_item_title(self):
        return self.items.first.element('.basket-item__title')

    @property
    def title(self):
        return browser.element('h1')

    def open(self):
        with allure.step("Открытие страницы корзины"):
            super().open()
