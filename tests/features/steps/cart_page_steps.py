from behave import *

from framework.configruration import screenshot_name_by_default
from framework.utils.logger_util import Logger
from tests.context import Context
from tests.utils.string_util import get_data_from_purchase
from framework.browser import Browser
from framework.utils.string_util import get_figures_from_string

use_step_matcher("parse")


@step('{gadget} in the cart')
def check_element_in_cart_correct(context, gadget):
    assert Context.cart_page.is_goods_correct_in_cart([gadget]), "elements are not correct"


@step("go back to the main page")
def go_to_main_page(context):
    Context.cart_page.go_to_the_main_page()


@then("notebook {dell_gadget} and {sony_gadget} in the cart")
def check_goods_in_cart(context, dell_gadget, sony_gadget):
    assert Context.cart_page.is_goods_correct_in_cart(
        [dell_gadget, sony_gadget]), "the cart contains not correct elements"


@when("delete {gadget} from the cart")
def delete_elem_from_cart(context, gadget):
    Context.cart_page.delete_element_from_cart(gadget)


@when("click place Order button")
def make_order(context):
    Context.total_price = Context.cart_page.get_total_price()
    Context.cart_page.make_order()


@then("place order is displayed")
def check_order_form_is_displayed(context):
    assert Context.cart_page.order_form_is_displayed(), "order form is not displayed"


@when("fill in all the fields by random data")
def fill_in_form(context):
    Context.cart_page.order_form.fill_all_the_fields_by_random_data()


@step("click Purchase button")
def step_impl(context):
    Context.cart_page.order_form.accept_purchase()


@step("take screen and log purchase {purchase_id} and {purchase_amount}")
def take_screenshot(context, purchase_id, purchase_amount):
    Browser().take_screenshot(screenshot_name_by_default)
    Context.data = get_data_from_purchase(Context.cart_page.sweet_alert.get_purchase_details())
    Logger.info(f"Purchase ID - {Context.data.get(purchase_id)};\n Amount - {Context.data.get(purchase_amount)}")


@then("{amount} and price is equal")
def check_price_and_amount(context, amount):
    price_from_receipt = get_figures_from_string(Context.data.get(amount))[0]
    assert price_from_receipt == Context.total_price, "prices are not equal"


@when("click OK")
def accept_purchase(context):
    Context.cart_page.sweet_alert.accept_purchase()


@step("cart is empty")
def check_cart_is_empty(context):
    assert Context.cart_page.get_count_elements_in_cart() == 0, "cart is not empty"
