from datetime import date, datetime
from sys import exit


class LogErrors:
    @staticmethod
    def logError(error: str, is_to_shut_down: bool = True):
        with open('LOG.txt', 'a') as log_file:
            timed_error = str(datetime.today()) + ': ' + error + '\n'
            log_file.write(timed_error)
            if is_to_shut_down:
                exit('Shutting Down! See LOG.txt')

