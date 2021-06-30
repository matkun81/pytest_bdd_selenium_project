from framework.utils.logger_util import Logger


def get_data_from_purchase(text):
    Logger.info(f"Purchase report was received:\n{text}")
    list_elements = list(text.split("\n"))
    result = {}
    for i in list_elements:
        k = i.split(":")
        result[k[0]] = k[1]
    return result


