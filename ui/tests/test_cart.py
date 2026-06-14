from selene import have, be

from ui.pages.cart_page import CartPage
from ui.pages.main_page import MainPage
from ui.pages.product_page import ProductPage
from ui.pages.search_results_page import SearchResultsPage


def test_add_book_to_cart():
    main_page = MainPage()
    results_page = SearchResultsPage()
    cart_page = CartPage()
    product_page = ProductPage()

    main_page.open()
    main_page.location_popup.accept_city()

    main_page.header.search_book("Мастер и Маргарита")

    results_page.first_book.click()
    product_page.title.should(be.visible)

    product_page.add_to_cart()

    cart_page.open()

    cart_page.items.should(have.size_greater_than(0))
    cart_page.first_item_title.should(have.text("Мастер"))


def test_open_cart_when_empty():
    main_page = MainPage()

    main_page.open()
    main_page.location_popup.accept_city()

    main_page.header.cart.should(
        have.attribute("class").value_containing("user-button-container--disabled")
    )


def test_open_cart_when_has_items():
    main_page = MainPage()
    results_page = SearchResultsPage()
    cart_page = CartPage()
    product_page = ProductPage()

    main_page.open()
    main_page.location_popup.accept_city()

    main_page.header.search_book("Мастер и Маргарита")

    results_page.first_book.click()
    product_page.title.should(be.visible)
    product_page.add_to_cart()

    cart = main_page.header.cart
    cart_count = main_page.header.cart_count

    cart_count.should(have.text("1"))

    cart.click()

    cart_page.title.should(have.text("Корзина"))


def test_cart_counter_updated_after_adding_book():
    main_page = MainPage()
    results_page = SearchResultsPage()
    product_page = ProductPage()

    main_page.open()
    main_page.location_popup.accept_city()

    main_page.header.search_book("Мастер и Маргарита")

    results_page.first_book.click()
    product_page.add_to_cart()

    main_page.header.cart_count.should(have.text("1"))
