from selenium.webdriver.common.by import By

from framework.base_page.base_page import BasePage
from framework.elements.button import Button


class DescriptionProduct(BasePage):
    add_to_cart_button = Button(By.XPATH, "//a[contains(@onclick,'addToCart')]", "add_cart_button")

    def __init__(self, name_of_element):
        super(DescriptionProduct, self).__init__(By.XPATH,
                                                 f"//div[@id='tbodyid']/h2[@class='name' and text()='{name_of_element}']",
                                                 "product_description_page")

    def add_product_to_cart(self):
        self.add_to_cart_button.click()
