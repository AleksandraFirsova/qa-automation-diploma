import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config.ui_config import UIConfig
from utils import attach


@pytest.fixture(scope='function', autouse=True)
def setup_browser():
    options = Options()

    options.set_capability("browserName", UIConfig.BROWSER)
    options.set_capability("browserVersion", UIConfig.BROWSER_VERSION)

    options.set_capability(
        "selenoid:options",
        {
            "enableVNC": True,
            "enableVideo": True,
            "screenResolution": f"{UIConfig.SCREEN_WIDTH}x{UIConfig.SCREEN_HEIGHT}x24",
            "name": "Bookvoed UI Tests",
        },
    )

    driver = webdriver.Remote(
        command_executor=UIConfig.SELENOID_URL,
        options=options,
    )

    driver.set_window_size(UIConfig.SCREEN_WIDTH, UIConfig.SCREEN_HEIGHT)

    browser.config.driver = driver
    browser.config.timeout = 10
    browser.config.window_maximized = True

    yield
    session_id = driver.session_id

    attach.add_screenshot(driver)
    attach.add_page_source(driver)
    attach.add_console_logs(driver)
    attach.add_video(session_id)

    driver.quit()
