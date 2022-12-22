from ProcessRunner import ProcessRunner


class Storage:
    def __init__(self):
        self.today_dict = None
        self. tomorrow_dict = None
        self.collected = False

    def reset(self):
        self.today_dict = None
        self.tomorrow_dict = None
        self.collected = False


class ServerJob:
    def __init__(self):
        self.global_storage: Storage = Storage()

        self.process_running_instance: ProcessRunner = ProcessRunner(global_storage_namespace=self.global_storage)

    def run(self):
        print('Running')
        self.process_running_instance.runProcess()

    def reset(self):
        self.global_storage.reset()


if __name__ == '__main__':
    pass


# Process each node to determine a value. The value should correspond to a bool, either true or false.
# Main should control that each process has finished before continuing

