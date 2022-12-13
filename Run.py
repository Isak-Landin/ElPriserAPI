from multiprocessing import Manager
from ProcessRunner import ProcessRunner

print(__name__)


class ServerJob:
    def __init__(self):
        self.global_data_manager: Manager = Manager()
        self.global_data_storage: Manager = self.global_data_manager.Namespace()

        self.process_running_instance: ProcessRunner = ProcessRunner(global_storage_namespace=self.global_data_storage)

    def run(self):
        print('Running')
        self.process_running_instance.runProcess()


if __name__ == '__main__':
    pass


# Process each node to determine a value. The value should correspond to a bool, either true or false.
# Main should control that each process has finished before continuing

