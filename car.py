


class Car(object):
    def __init__(self, idx, streets, totalPath, inters):
        # self.intersect
        self.idx = idx
        self.streets = streets
        self.inters = inters
        self.totalPath = totalPath
        # self.nPath = 

    def __repr__(self):
        return "({}/{}/S:{}/I:{})".format(
            self.idx, self.totalPath, 
            '='.join(self.streets), 
            '_'.join([str(x) for x in self.inters]))