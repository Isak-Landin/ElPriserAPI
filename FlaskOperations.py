import datetime
import os
import json
from LogErrors import LogErrors
import traceback


class Operations:
    @staticmethod
    def getJsonPriceContents():
        name_of_new_file = 'Collected' + str(datetime.date.today()) + '.json'
        path_to_store_file = str(os.path.abspath(os.getcwd())) + r'\JSONFiles' + fr'\{name_of_new_file}'

        """TEMPORARY FILE"""
        path_to_store_file = str(os.path.abspath(os.getcwd())) + r'\JSONFiles' + fr'\test.json'
        """TEMPORARY FILE"""
        price_dict: dict = {}

        try:
            with open(path_to_store_file) as file:
                price_dict: dict = json.load(file)
        except FileExistsError:
            error: str = traceback.format_exc()
            LogErrors.logError(error)
        except FileNotFoundError:
            error: str = traceback.format_exc()
            LogErrors.logError(error)
        finally:
            return price_dict

    @staticmethod
    def getErrorContents():
        error_messages: str = ''
        log_file: str = str(os.path.abspath(os.getcwd())) + r'\LOG.txt'

        try:
            with open(log_file) as file:
                error_messages: str = file.read()
        except FileExistsError:
            error: str = traceback.format_exc()
            LogErrors.logError(error)
        except FileNotFoundError:
            error: str = traceback.format_exc()
            LogErrors.logError(error)
        finally:
            return error_messages

