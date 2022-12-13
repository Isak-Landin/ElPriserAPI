import multiprocessing
from multiprocessing import Manager
import time
from enum import Enum
from Collector import Collector


class ProcessController:
    def __init__(self, global_storage_object: Manager):
        self.data_storage = global_storage_object.Namespace()
        self.process_array = []

    @staticmethod
    def startProcess(method_to_be_called, *args):
        process = multiprocessing.Process(target=method_to_be_called, args=args)
        return process

    def addProcess(self, process_to_add: multiprocessing.Process):
        self.process_array.append(process_to_add)

    def removeProcess(self, process_to_remove: multiprocessing.Process):
        # remove process of value:::
        try:
            self.process_array.remove(process_to_remove)
            return
        except TypeError:
            raise TypeError
        except ValueError:
            raise ValueError
        except NameError:
            raise NameError

    def confirmFinishedProcess(self, process_to_confirm: multiprocessing.Process, time_started=None, max_time_allowed=None):
        if process_to_confirm in self.process_array:
            if time_started and max_time_allowed:
                if time.time() > time_started + max_time_allowed:
                    process_to_confirm.terminate()
                    self.process_array.remove(process_to_confirm)
                    return ResponseTypes.TERMINATED

            if process_to_confirm.is_alive():
                return ResponseTypes.NOTFINISHED
            else:
                self.removeProcess(process_to_confirm)
                return ResponseTypes.FINISHED
        else:
            raise IndexError


class CollectionProcess:
    def __init__(self, process_controller_instance: ProcessController, collector_node: Collector):
        self.process_controller = process_controller_instance
        self.corresponding_node = collector_node



class ResponseTypes(Enum):
    FINISHED = 1
    NOTFINISHED = 2
    TERMINATED = 3



