from ui.components.header import Header
from ui.components.location_popup import LocationPopup
from ui.pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self):
        self.location_popup = LocationPopup()
        self.header = Header()
