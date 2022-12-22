import requests
import traceback
from LogErrors import LogErrors
from datetime import date
from Runner import Storage
from ElSpotTodayPricesScraper import ScrapeElSpot
from Sorter import Sorter

import json


class Collector:
    def __init__(self, next_process: Sorter, *args, **kwargs):
        super(Collector, self).__init__(*args, **kwargs)
        self.global_storage_namespace: Storage = None
        self.ElSpotScraper: ScrapeElSpot = ScrapeElSpot()

        self.value = False
        self.next_node: Sorter = next_process
    
    @staticmethod
    def GetTomorrowsDate(today: date):
        today_date: str = str(today)
        today_last_number = int(today_date[-1])

        tomorrows_date = today_date[:-1:] + str(today_last_number + 1)

        return tomorrows_date

    def CollectData(self):
        try:
            tomorrows_data = requests.get(f'https://mgrey.se/espot?format=json&date={self.GetTomorrowsDate(date.today())}')
            if tomorrows_data:
                tomorrows_data = tomorrows_data.json()
            today_data: dict = self.ElSpotScraper.todayDataProcessCollectSort()
            return today_data, tomorrows_data
        except ConnectionError:
            error: str = traceback.format_exc()
            LogErrors.logError(error)
        except TypeError:
            error: str = traceback.format_exc()
            LogErrors.logError(error)
        except ValueError:
            error: str = traceback.format_exc()
            LogErrors.logError(error)

    def StoreRawDataInGlobalStorage(self, today_to_store: dict, tomorrow_to_store: dict):
        try:
            today_contains: bool = bool(today_to_store)
            tomorrow_contains: bool = bool(tomorrow_to_store)
            if today_contains and tomorrow_contains and self.global_storage_namespace:
                self.global_storage_namespace.collected = True
                self.global_storage_namespace.today_dict = today_to_store
                self.global_storage_namespace.tomorrow_dict = tomorrow_to_store
                self.value = True

        except TypeError:
            error: str = traceback.format_exc()
            LogErrors.logError(error)
        except ValueError:
            error: str = traceback.format_exc()
            LogErrors.logError(error)

    def assignGlobalStorage(self, global_storage_namespace: Storage):
        self.global_storage_namespace = global_storage_namespace

    def entireProcess(self):
        today_collected, tomorrow_collected = self.CollectData()
        self.StoreRawDataInGlobalStorage(today_to_store=today_collected, tomorrow_to_store=tomorrow_collected)

        if self.value:
            self.next_node.value = True
