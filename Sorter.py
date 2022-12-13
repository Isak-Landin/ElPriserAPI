import json
from multiprocessing import Manager
import datetime
import os
from LogErrors import LogErrors
import traceback


class FileAlreadyExistsException(Exception):
    def __init__(self, file_name: str, message: str = 'File Already Exists'):
        self.message = message
        self.file_name = file_name

        self.new_message = message + ': ' + file_name

        self.logFileAlreadyInExistence(self.new_message)
        super().__init__(self.new_message)

    @staticmethod
    def logFileAlreadyInExistence(log_error: str):
        LogErrors.logError(log_error)


class Sorter:
    def __init__(self, *args, **kwargs):
        super(Sorter, self).__init__(*args, **kwargs)
        self.global_storage = None
        self.value: bool = False

    def assignGlobalStorageNamespace(self, global_storage_name_space: Manager):
        self.global_storage = global_storage_name_space

    def checkForAllowanceToRun(self):
        allowance: bool = False
        if self.global_storage.collected and bool(self.global_storage.today_dict['Today']) and\
                bool(self.global_storage.tomorrow_dict) and self.value:
            try:
                if self.global_storage.tomorrow_dict['SE4']:
                    try:
                        tomorrow_dict_malmo = self.global_storage.tomorrow_dict['SE4']
                        if tomorrow_dict_malmo is not None:
                            allowance = True
                    except AttributeError:
                        print('AttributeError')
                        error: str = traceback.format_exc()
                        LogErrors.logError(error)
                    except ValueError:
                        print('ValueError')
                        error: str = traceback.format_exc()
                        LogErrors.logError(error)
                    except IndexError:
                        print('IndexError')
                        error: str = traceback.format_exc()
                        LogErrors.logError(error)
            except AttributeError:
                print('AttributeError')
                error: str = traceback.format_exc()
                LogErrors.logError(error)

            except ValueError:
                print('ValueError')
                error: str = traceback.format_exc()
                LogErrors.logError(error)

            except IndexError:
                print('IndexError')
                error: str = traceback.format_exc()
                LogErrors.logError(error)

        return allowance

    def sortToRelevantFormat(self):
        dict_to_sort = self.global_storage.tomorrow_dict
        after_process_dict: dict = {
            'Tomorrow': {}
        }

        for data_set in dict_to_sort:
            after_process_dict['Tomorrow'][data_set['hour']] = data_set['price_sek']

        if bool(after_process_dict):
            return {**after_process_dict, **self.global_storage.today_dict}
        else:
            return None

    @staticmethod
    def getTomorrowsDate():
        return datetime.date.today() + datetime.timedelta(days=1)

    @staticmethod
    def storeWithRelevantName(data_to_store: dict):
        name_of_new_file = 'Collected' + str(datetime.date.today()) + '.json'

        path_to_store_file = str(os.path.abspath(os.getcwd())) + r'\JSONFiles' + fr'\{name_of_new_file}'
        is_file_exist: bool = os.path.exists(path_to_store_file)

        if is_file_exist:
            raise FileAlreadyExistsException(file_name=path_to_store_file)
        else:
            with open(path_to_store_file, 'w+') as file:
                json.dump(data_to_store, file)

        return path_to_store_file

    def entireProcess(self):
        file_path: str = ''
        if self.value:
            allowance = self.checkForAllowanceToRun()
            if allowance:
                data_to_store = self.sortToRelevantFormat()
                if data_to_store is not None:
                    file_path = self.storeWithRelevantName(data_to_store)

        return os.path.exists(file_path)

