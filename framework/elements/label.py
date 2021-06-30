from framework.elements.base_element.base_element import BaseElement


class Label(BaseElement):
    def __init__(self, search_condition, locator, name_element):
        super().__init__(search_condition, locator, name_element)
