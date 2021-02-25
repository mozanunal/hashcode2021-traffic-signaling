

class Street(object):
    def __init__(self, start, end, name, lenght):
        self.start = int(start)
        self.end = int(end)
        self.name = name
        self.lenght = int(lenght)
        self.numCar = 0


        # sols = []
        # for street, num in inter.solution2.items():
        #     sols.append( {'name':street, 'score':num} )
        # sols = sorted(sols, key=itemgetter('score'), reverse=True)

        # for obj in sols:
        #     f.write('{} {}\n'.format(obj['name'], obj['score']))