from Collector import Collector
from Sorter import Sorter
from multiprocessing import Manager
from LogErrors import LogErrors
import traceback
from datetime import datetime


class ProcessRunner:
    def __init__(self, global_storage_namespace: Manager = None):
        self.global_data_storage: Manager = global_storage_namespace
        self.sorter_instance = Sorter()
        self.sorter_instance.assignGlobalStorageNamespace(self.global_data_storage)
        self.collector_instance = Collector(next_process=self.sorter_instance)
        self.collector_instance.assignGlobalStorage(self.global_data_storage)
        self.start_time: str = '13:30'
        self.end_time: str = '15:00'

    def runProcess(self):
        has_run: bool = False
        if self.isTimeCorrect():
            while not has_run:
                self.collector_instance.entireProcess()
                has_run = self.sorter_instance.entireProcess()

    def isTimeCorrect(self):
        is_good_to_go: bool = False
        if self.convertStrTimeToDoubleTime(time=self.timeNowHourMinute()) > 13.5 and\
                self.convertStrTimeToDoubleTime(self.timeNowHourMinute()) < 15.0:
            is_good_to_go = True

        return is_good_to_go

    @staticmethod
    def convertStrTimeToDoubleTime(time: str) -> float:
        try:
            time_slices: list = time.split(sep=':')
            hour: str = time_slices[0]
            minute: str = time_slices[1]
            minute_share: float = int(minute)/60
            return float(hour) + minute_share
        except IndexError:
            error: str = traceback.format_exc()
            LogErrors.logError(error)
        except AttributeError:
            error: str = traceback.format_exc()
            LogErrors.logError(error)
        except ValueError:
            error: str = traceback.format_exc()
            LogErrors.logError(error)

    @staticmethod
    def timeNowHourMinute():
        return datetime.now().strftime("%H:%M")

