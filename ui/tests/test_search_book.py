from selene import have

from ui.pages.main_page import MainPage
from ui.pages.search_results_page import SearchResultsPage


def test_search_book():
    main_page = MainPage()
    results_page = SearchResultsPage()

    main_page.open("https://www.bookvoed.ru")
    main_page.location_popup.accept_city()
    main_page.header.search_book("Мастер и Маргарита")
    results_page.first_book.should(have.text("Мастер"))


def test_search_nonexistent_book():
    main_page = MainPage()
    results_page = SearchResultsPage()

    main_page.open("https://www.bookvoed.ru")
    main_page.location_popup.accept_city()

    main_page.header.search_book("asldkjasldkjasldkj123123")

    results_page.empty_result.should(have.text("Мы не нашли такой товар"))
