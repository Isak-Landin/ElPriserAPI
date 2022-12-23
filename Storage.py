class Storage:
    def __init__(self):
        self.today_dict = None
        self. tomorrow_dict = None
        self.collected = False

    def reset(self):
        self.today_dict = None
        self.tomorrow_dict = None
        self.collected = False