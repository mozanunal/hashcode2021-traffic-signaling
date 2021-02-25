

class Inter(object):
    def __init__(self, idx):
        self.idx = idx
        self.cars = []
        self.upComm = []
        self.inComm = []
        self.solution = {}

    def __repr__(self):
        return '({}/S:{})'.format(self.idx, '='.join([x.name for x in self.upComm]) )