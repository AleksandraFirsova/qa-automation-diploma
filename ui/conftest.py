import pytest

from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()

    options.set_capability("browserName", "chrome")
    options.set_capability("browserVersion", "127.0")

    options.set_capability(
        "selenoid:options",
        {
            "enableVNC": True,
            "enableVideo": True,
            "screenResolution": "1920x1080x24",
            "name": "Bookvoed UI Tests",
        },
    )

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,
    )

    driver.set_window_size(1920, 1080)

    browser.config.driver = driver
    browser.config.timeout = 10
    browser.config.window_maximized = True

    yield

    driver.quit()
