from behave import *

from tests.context import Context
from framework.browser import Browser
from pages.description_product_page import DescriptionProduct

use_step_matcher("parse")


@then("{gadget} is displayed")
def then_gadget_is_displayed(context, gadget):
    Context.description_page = DescriptionProduct(gadget)


@step("click on Add to cart")
def add_good_to_cart(context):
    Context.description_page.add_product_to_cart()


@step("accept pop up information")
def accept_pop_information(context):
    Browser().accept_alert()

