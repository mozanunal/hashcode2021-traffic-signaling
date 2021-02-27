from operator import itemgetter, attrgetter
from car import Car
from street import Street
from intersect import Inter
from tqdm import tqdm
import numpy as np

def dump(filename, interList):
    f = open(filename.replace('.txt', '.out').replace('input/', 'output/'), 'w+')
    filteredInters = []
    for inter in interList:
        if len(inter.solution2) > 0:
            filteredInters.append(inter)
    
    f.write('{}\n'.format(len(filteredInters)))
    for inter in filteredInters:
        f.write('{}\n'.format(inter.idx))
        f.write('{}\n'.format(len(inter.solution2)))
        for street, num in inter.solution2.items():
            f.write('{} {}\n'.format(street, num))
    f.close()

def solve( interList, streetList, carList, avgStreetLenght):
    for inter in interList:
        total = 0
        for street in inter.inComm:
            if street.numCar != 0:
                inter.solution[street.name] = street.numCar
                total += street.numCar #/street.lenght
        
        norm = 5
        for streetName, num in inter.solution.items():
            if int(norm * num/total) > 1:
                inter.solution2[streetName] = int(norm * num/total)
            else:
                inter.solution2[streetName] = 1

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
        for path in paths:
            totalPath+= streetList[path].lenght
        car = Car(i, paths, totalPath, inters)
        carList.append(
            car
        )
    
    carList = sorted(carList, key=attrgetter('totalPath')) 

    for car in carList[0:nCar//10]:
        for street in car.streets:
            streetList[street].numCar += 50

    for car in carList[nCar//10:nCar]:
        for street in car.streets:
            streetList[street].numCar += 1


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


    solve( interList, streetList, carList, avgStreetLenght)
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
