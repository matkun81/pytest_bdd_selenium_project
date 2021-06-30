from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from framework.browser_factory import BrowserFactory
from framework.configruration import EXPLICIT_WAIT
from framework.singleton import Singleton
from framework.utils.logger_util import Logger


class Browser(metaclass=Singleton):
    def __init__(self):
        self.__driver = BrowserFactory.get_browser()

    def get_driver(self):
        return self.__driver

    def get_url(self, url):
        self.get_driver().get(url)

    def get_alert(self):
        Logger.info("Getting Alert")
        return WebDriverWait(self.__driver, EXPLICIT_WAIT).until(ec.alert_is_present())

    def accept_alert(self):
        alert = self.get_alert()
        Logger.info("Accepting alert")
        alert.accept()

    def take_screenshot(self, file_name):
        Logger.info(f"take screen with name: {file_name}")
        self.__driver.get_screenshot_as_file(file_name)
        self.__driver.save_screenshot(file_name)
