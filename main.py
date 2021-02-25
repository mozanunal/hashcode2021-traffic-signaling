
from car import Car
from street import Street
from intersect import Inter
from tqdm import tqdm
import numpy as np

def dump(filename, interList):
    f = open(filename.replace('.txt', '.out'), 'w+')
    filteredInters = []
    for inter in interList:
        if len(inter.solution) > 0:
            filteredInters.append(inter)
    
    f.write('{}\n'.format(len(filteredInters)))
    for inter in filteredInters:
        f.write('{}\n'.format(inter.idx))
        f.write('{}\n'.format(len(inter.solution)))
        for street, num in inter.solution.items():
            f.write('{} {}\n'.format(street, num))
    f.close()

def solve( interList, streetList, carList):
    for inter in interList:
        for street in inter.inComm:
            score = street.numCar
            if score != 0:
                inter.solution[street.name] = street.numCar * street.lenght
        print(inter.idx, ['{}:{}'.format(x.name,x.numCar) for x in inter.inComm])

def readF(filename):
    f = open(filename)

    nSim, nInter, nStreet, nCar, bonus = [int(x) for x in  f.readline().split(' ')]
    interList = []
    streetList = {}
    carList = []

    for i in range(nInter):
        interList.append(
            Inter(i)
        )

    for i in range(nStreet):
        start, end, name, lenght = f.readline().replace('\n','').split(' ')
        street = Street(start,end,name,lenght)
        streetList[name] = street

    for i in range(nCar):
        paths = f.readline().replace('\n','').split(' ')[1:]
        totalPath = 0
        inters = []
        for path in paths:
            inters.append(
                streetList[path].end
            )
        for path in paths[1:]:
            totalPath+= streetList[path].lenght
            streetList[path].numCar += 1 
        car = Car(i, paths[1:], totalPath, inters)
        carList.append(
            car
        )

    for name, street in streetList.items():
        interList[street.start].upComm.append(streetList[name])
        interList[street.end].inComm.append(streetList[name])

    avgTotalPath = np.mean([x.totalPath for x in carList])
    avgStreetLenght = np.mean( [streetList[x].lenght for x in streetList])
    

    print('------', filename)
    print("-- nSim", nSim )
    print("-- nInter", nInter )
    print("-- nStreet", nStreet )
    print("-- nStreet/nInter", nStreet/nInter)
    print("-- nStreet avg len", avgStreetLenght)
    print("-- nCar", nCar )
    print("-- nCar totalpath avg", avgTotalPath)
    print("-- bonus", bonus )


    solve( interList, streetList, carList)
    dump(filename, interList)
    # for i in range(nInter):
    #     print(interList[i])



# filename = 'input/a.txt'
readF('input/a.txt')
readF('input/b.txt')
readF('input/c.txt')
readF('input/d.txt')
readF('input/e.txt')
readF('input/f.txt')
# 
