from display_update import DisplayUpdate


class Algorithm:
    """ Base algorithm class """
    def __init__(self, array, socket):
        self.array = array
        self.socket = socket
        self.swaps = {}
        self.display_updater = DisplayUpdate(self.array, self.socket)
        self.stopped = False

    def run_algorithm(self):
        self.algorithm()

    @classmethod
    def get_name(cls):
        return cls.name
