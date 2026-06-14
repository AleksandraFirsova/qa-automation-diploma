from selene import browser

from ui.components.close_popmechanic_popup import PopmechanicPopup
from ui.pages.base_page import BasePage


class SearchResultsPage(BasePage):

    def __init__(self):
        self.popmechanic_popup = PopmechanicPopup()

    @property
    def books(self):
        return browser.all('[data-product-name]')

    @property
    def first_book(self):
        return self.books.first

    @property
    def empty_result(self):
        return browser.element('.empty-products__title')
