from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from framework.browser import Browser
from framework.configruration import EXPLICIT_WAIT
from framework.utils.logger_util import Logger


class BaseElement:
    def __init__(self, search_condition, locator, name_of_element):
        self.search_condition = search_condition
        self.locator = locator
        self.name_of_element = name_of_element

    def get_element_name(self):
        return self.name_of_element

    def find_element(self):
        return WebDriverWait(Browser().get_driver(), EXPLICIT_WAIT,
                             ignored_exceptions=StaleElementReferenceException).until(
            ec.presence_of_element_located((self.search_condition, self.locator)))

    def click(self):
        element = self.find_element()
        element.click()

    def get_text(self):
        element = self.find_element()
        return element.text

    def find_elements(self):
        WebDriverWait(Browser().get_driver(), EXPLICIT_WAIT,
                      ignored_exceptions=StaleElementReferenceException).until(
            ec.visibility_of_all_elements_located((self.search_condition, self.locator)))
        return Browser().get_driver().find_elements(self.search_condition, self.locator)

    def get_count_found_elements(self):
        try:
            count_elements = len(self.find_elements())
            Logger.info(f"{count_elements} was found by {self.search_condition} and {self.locator}")
        except TimeoutException:
            Logger.info("Elements not found")
            return 0
        return count_elements

    def wait_till_get_invisible(self):
        WebDriverWait(Browser().get_driver(), timeout=EXPLICIT_WAIT).until(
            ec.invisibility_of_element((self.search_condition, self.locator)))

    def wait_for_presence(self):
        WebDriverWait(Browser().get_driver(), EXPLICIT_WAIT,
                      ignored_exceptions=StaleElementReferenceException).until(
            ec.presence_of_element_located((self.search_condition, self.locator)))

    def wait_for_visible(self):
        WebDriverWait(Browser().get_driver(), EXPLICIT_WAIT,
                      ignored_exceptions=StaleElementReferenceException).until(
            ec.visibility_of_element_located((self.search_condition, self.locator)))

    def is_present(self):
        try:
            WebDriverWait(Browser().get_driver(), EXPLICIT_WAIT,
                          ignored_exceptions=StaleElementReferenceException).until(
                ec.presence_of_element_located((self.search_condition, self.locator)))
        except NoSuchElementException:
            Logger.info("Element is not present")
            return False
        return True
