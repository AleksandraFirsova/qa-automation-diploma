from selene import have

from ui.pages.main_page import MainPage
from ui.pages.product_page import ProductPage
from ui.pages.search_results_page import SearchResultsPage


def test_product_page_content():
    main_page = MainPage()
    results_page = SearchResultsPage()
    product_page = ProductPage()

    main_page.open("https://www.bookvoed.ru")
    main_page.location_popup.accept_city()

    main_page.header.search_book("Мастер и Маргарита")

    results_page.first_book.click()

    product_page.title.should(have.text("Мастер"))
    product_page.price.should(have.attribute('textContent').value_containing(''))
    product_page.images.should(have.size_greater_than(0)).first.should(have.attribute('src'))
