import allure
from selene import browser, be


class Header:
    @property
    def cart(self):
        return browser.element('a[href="/personal/cart"]')

    @property
    def cart_count(self):
        return browser.element('a[href="/personal/cart"] span')

    search_input = browser.element('[name="search"]')
    search_button = browser.element("button[type='submit']")

    def search_book(self, book_name: str):
        with allure.step(f"Поиск книги: {book_name}"):
            with allure.step("Ожидание видимости поля поиска и ввод текста"):
                self.search_input.should(be.visible).type(book_name)

            with allure.step("Нажатие кнопки поиска"):
                self.search_button.click()

            with allure.step("Ожидание готовности результатов поиска"):
                browser.element('[data-product-name]').should(be.visible)

    def search_book_expect_no_results(self, book_name: str):
        with allure.step(f"Поиск книги (ожидаем отсутствие результата): {book_name}"):
            with allure.step("Ожидание видимости поля поиска и ввод текста"):
                self.search_input.should(be.visible).type(book_name)

            with allure.step("Нажатие кнопки поиска"):
                self.search_button.click()

            with allure.step("Проверка отсутствия результатов"):
                browser.element('[data-product-name]').should(be.not_.visible)
