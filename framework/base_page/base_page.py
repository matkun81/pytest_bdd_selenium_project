from framework.elements.label import Label
from framework.utils.logger_util import Logger


class BasePage:
    def __init__(self, search_condition, locator, page_name):
        self.locator = locator
        self.page_name = page_name
        self.search_condition = search_condition

    def wait_page_to_load(self):
        Logger.info("Waiting for opening page... " + self.page_name)
        Label(self.search_condition, self.locator, self.page_name).wait_for_visible()

    def is_opened(self):
        Logger.info("Checking page is opened " + self.page_name)
        self.wait_page_to_load()
        return Label(self.search_condition, self.locator, self.page_name).is_present()
