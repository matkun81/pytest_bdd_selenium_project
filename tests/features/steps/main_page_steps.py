from behave import *

from tests.context import Context
from framework.browser import Browser
from framework.configruration import url
from pages.main_page import MainPage


@step("open Main page")
def open_main_page(context):
    Browser().get_url(url)
    Context.main_page = MainPage()
    assert Context.main_page.is_opened(), "The main page was not opened"


@step("categories: Phones, Laptops, Monitors are displayed")
def check_categories_is_displayed(context):
    Context.main_page.is_categories_displayed()


@step("click on category Laptops")
def chose_laptop_category(context):
    Context.main_page.get_laptops_category()


@step("click on notebook {name_elem}")
def chose_good_in_page(context, name_elem):
    Context.main_page.go_to_elem_description(name_elem)


@step("go to the cart")
def go_to_cart(context):
    Context.main_page.go_to_the_cart()


@then("Main Page is opened")
def check_main_page_is_opened(context):
    assert Context.main_page.is_opened(), "The main page is not downloaded"
