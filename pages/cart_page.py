from selenium.webdriver.common.by import By

from framework.base_page.base_page import BasePage
from framework.elements.button import Button
from framework.elements.input import Input
from framework.elements.label import Label
from framework.utils.logger_util import Logger
from framework.utils.string_util import random_string
from pages.main_page import NavigationBar


class SweetAlert(BasePage):
    purchase_details = Input(By.XPATH, "//p[contains(@class, 'text-muted')]", "purchase_details")
    ok_button = Button(By.XPATH, "//div[contains(@class,'sa-confirm-button')]", "ok_button")

    def __init__(self):
        super(SweetAlert, self).__init__(By.XPATH,
                                         "//div[contains(@class,'showSweetAlert') and contains(@class,'visible')]",
                                         "sweet_alert_form")

    def get_purchase_details(self):
        return self.purchase_details.get_text()

    def accept_purchase(self):
        self.ok_button.click()


class OrderForm(BasePage):
    name_field = Input(By.XPATH, "//input[@id='name']", "name_field")
    country_field = Input(By.XPATH, "//input[@id='country']", "country_field")
    city_field = Input(By.XPATH, "//input[@id='city']", "city_field")
    card_field = Input(By.XPATH, "//input[@id='card']", "card_field")
    month_field = Input(By.XPATH, "//input[@id='month']", "month_field")
    year_field = Input(By.XPATH, "//input[@id='year']", "year_field")

    purchase_button = Button(By.XPATH, "//button[@onclick='purchaseOrder()']", "purchase_button")

    def __init__(self):
        super(OrderForm, self).__init__(By.XPATH, "//div[@id='orderModal' and contains(@class,'show')]", "order_form")

    def fill_all_the_fields_by_random_data(self):
        self.name_field.insert_text(random_string())
        self.country_field.insert_text(random_string())
        self.city_field.insert_text(random_string())
        self.card_field.insert_text(random_string())
        self.month_field.insert_text(random_string())
        self.year_field.insert_text(random_string())

    def accept_purchase(self):
        self.purchase_button.click()


class CartPage(BasePage):
    delete_button = None
    nav_bar = NavigationBar()
    order_form = OrderForm()
    sweet_alert = SweetAlert()
    elem_in_cart = Label(By.XPATH, "//tr[@class='success']/td[2]", "elem_in_cart_in_cart")
    list_goods_in_cart = Label(By.CLASS_NAME, "success", "count_elements")
    total_price_label = Label(By.ID, "totalp", "total_price_label")
    order_button = Button(By.XPATH, "//button[@data-target='#orderModal']", "order_button")

    def __init__(self):
        super(CartPage, self).__init__(By.CLASS_NAME, "table-responsive", "cart_page")

    def get_name_elem_in_cart(self):
        self.elem_in_cart.wait_for_visible()
        return self.elem_in_cart.get_text()

    def get_count_elements_in_cart(self):
        return self.list_goods_in_cart.get_count_found_elements()

    def go_to_the_main_page(self):
        self.nav_bar.logo.click()

    def is_goods_correct_in_cart(self, list_name_in_cart_must_be):
        list_names_elements_in_cart = [i.text for i in self.elem_in_cart.find_elements()]
        list_name_in_cart_must_be.sort()
        list_names_elements_in_cart.sort()
        Logger.info(f"Elements located in cart: {list_names_elements_in_cart}")
        Logger.info(f"The following elements must be in cart: {list_name_in_cart_must_be}")
        return list_name_in_cart_must_be == list_names_elements_in_cart

    def delete_element_from_cart(self, name_of_product):
        self.delete_button = Button(By.XPATH, f"//td[text()='{name_of_product}']/following::td[2]/a", "delete_button")
        self.delete_button.click()
        self.delete_button.wait_till_get_invisible()

    def get_total_price(self):
        return self.total_price_label.get_text()

    def make_order(self):
        self.order_button.click()

    def order_form_is_displayed(self):
        return self.order_form.is_opened()

    def sweet_alert_is_displayed(self):
        return self.sweet_alert.is_opened()
