import logging


class Logger:
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

    @staticmethod
    def info(str_, *args, **kwargs):
        logging.info(str_)

    @staticmethod
    def error(str_, *args, **kwargs):
        logging.error(str_)

    @staticmethod
    def list_log_output(object_list):
        for i in object_list:
            Logger.info(i.__dict__)