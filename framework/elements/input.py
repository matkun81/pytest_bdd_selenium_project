from framework.elements.base_element.base_element import BaseElement
from framework.utils.logger_util import Logger


class Input(BaseElement):
    def __init__(self, search_condition, locator, name_element):
        super().__init__(search_condition, locator, name_element)

    def insert_text(self, text):
        Logger.info(f"{text} was insert in {self.name_of_element}")
        self.find_element().send_keys(text)
