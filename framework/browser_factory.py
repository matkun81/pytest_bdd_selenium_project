from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from framework.configruration import browser, Browser
from framework.utils.logger_util import Logger


class BrowserFactory:
    @staticmethod
    def get_browser(capabilities=None):
        if capabilities is None:
            capabilities = {}
        if browser == Browser.CHROME:
            Logger.info("Driver chrome is initialized")
            return webdriver.Chrome(ChromeDriverManager().install(), desired_capabilities=capabilities)
        elif browser == Browser.FIREFOX:
            Logger.info("Driver firefox is initialized")
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), desired_capabilities=capabilities)
        else:
            Logger.error("Driver is not initialized")
            raise Exception("Driver is not initialized")
