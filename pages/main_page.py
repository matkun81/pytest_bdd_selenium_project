from selenium.webdriver.common.by import By

from framework.base_page.base_page import BasePage
from framework.elements.button import Button


class NavigationBar(BasePage):
    logo = Button(By.ID, "nava", "logo")
    cart_button = Button(By.ID, "cartur", "cart_button")

    def __init__(self):
        super().__init__(By.ID, 'nava', "nav_bar")


class MainPage(BasePage):
    nav_bar = NavigationBar()
    phone_category_button = Button(By.XPATH, "//a[@onclick=\"byCat('phone')\"]", "phone_category")
    note_book_category_button = Button(By.XPATH, "//a[@onclick=\"byCat('notebook')\"]", "note_book_category")
    monitor_category_button = Button(By.XPATH, "//a[@onclick=\"byCat('monitor')\"]", "monitors_category")
    good_in_page = None

    def __init__(self):
        super().__init__(By.ID, 'cat', "main_page")

    def get_laptops_category(self):
        self.note_book_category_button.click()

    def go_to_elem_description(self, name_of_good):
        self.good_in_page = Button(By.XPATH, f"//a[text()='{name_of_good}']", "good_in_page")
        self.good_in_page.click()

    def go_to_the_cart(self):
        self.nav_bar.cart_button.click()

    def is_categories_displayed(self):
        return self.phone_category_button.is_present() \
               and self.note_book_category_button.is_present() \
               and self.monitor_category_button.is_present()
