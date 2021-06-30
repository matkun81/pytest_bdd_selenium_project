import random
import re
import string

from framework.utils.logger_util import Logger


def get_figures_from_string(text):
    Logger.info(f"The following text was received: {text}")
    figures = re.findall('\d+', text)
    Logger.info(f"The following figure was received after processing: {figures}")
    return figures


def random_string(count=10):
    random_str = string.digits + string.ascii_letters
    return ''.join(random.sample(random_str, count))
