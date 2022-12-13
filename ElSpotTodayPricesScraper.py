import traceback
from datetime import datetime, date
from LogErrors import LogErrors
import requests
from bs4 import BeautifulSoup as bs


class ScrapeElSpot:
    def __init__(self):
        self.cost_time: dict = {
            'Today': {}
        }
        self.all_costs = []
        self.all_times = []
        self.soup = None

    def get_html(self):
        r = requests.get('https://elspot.nu/dagens-spotpris/timpriser-pa-elborsen-for-elomrade-se4-malmo/')

        self.soup = bs(r.content, features='html.parser')

    def grab_and_sort_collected_html(self):
        for child in self.soup.findChildren('tbody'):
            for tr_container in child:
                for td_container in tr_container:
                    try:
                        if 'öre/kWh' in td_container.text:
                            self.all_costs.append(td_container.text)

                        elif str(date.today()) in td_container.text:
                            clock = td_container.text[11:]
                            self.all_times.append(str(clock))

                    except AttributeError:
                        print("AttributeError")
                        error: str = traceback.format_exc()
                        if "AttributeError: 'str' object has no attribute 'text'" not in error:
                            LogErrors.logError(error)
                    except TypeError:
                        print("TypeError")
                        error: str = traceback.format_exc()
                        LogErrors.logError(error)
                    except IndexError:
                        print('IndexError')
                        error: str = traceback.format_exc()
                        LogErrors.logError(error)

        try:
            if len(self.all_costs) == len(self.all_times) and len(self.all_costs) > 0 and len(self.all_times) > 0:
                counter: int = 0
                for cost in self.all_costs:
                    self.cost_time['Today'][self.all_times[counter]] = cost
                    counter += 1
        except IndexError:
            print('IndexError')
            error: str = traceback.format_exc()
            LogErrors.logError(error)
        except ValueError:
            print('ValueError')
            error: str = traceback.format_exc()
            LogErrors.logError(error)
        except TypeError:
            print('TypeError')
            error: str = traceback.format_exc()
            LogErrors.logError(error)

    def todayDataProcessCollectSort(self):
        try:
            self.get_html()
            self.grab_and_sort_collected_html()
            return self.cost_time
        except Exception as error:
            LogErrors.logError(str(error))
