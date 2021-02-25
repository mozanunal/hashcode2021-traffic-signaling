

class Street(object):
    def __init__(self, start, end, name, lenght):
        self.start = int(start)
        self.end = int(end)
        self.name = name
        self.lenght = int(lenght)
        self.numCar = 0