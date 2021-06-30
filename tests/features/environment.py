from behave import fixture, use_fixture

from framework.browser import Browser
from framework.configruration import IMPLICIT_WAIT
from framework.utils.logger_util import Logger


@fixture
def browser(context):
    Logger.info("start browser...")
    context.browser = Browser().get_driver()
    context.browser.implicitly_wait(IMPLICIT_WAIT)
    context.browser.maximize_window()
    yield context.browser
    Logger.info("quit browser...")
    context.browser.quit()


def before_feature(context, args):
    use_fixture(browser, context)
