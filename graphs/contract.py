from random import randint
from math import log
from copy import deepcopy

contractionCount = 1

def numIterations(n):
    return (n ** 2) * log(n)

def contract(adjList):
    global contractionCount

    keys = adjList.keys()
    len_keys = len(keys)

    if len_keys <= 2:
        return len(adjList.values()[0])

    index1 = randint(0, len_keys - 1)
    index2 = randint(0, len_keys - 1)

    while index2 == index1:
        index2 = randint(0, len_keys - 1)

    # print "index 1:", index1
    # print "index 2:", index2

    # Merges the two vertices
    keyOne = keys[index1]
    keyTwo = keys[index2]

    valsOne = adjList[keyOne]
    valsTwo = adjList[keyTwo]

    # Deletes entries
    del adjList[keyOne]
    del adjList[keyTwo]

    values = [v for v in valsOne + valsTwo if v != keyOne and v != keyTwo]

    newIndex = "c" + str(contractionCount)
    adjList[newIndex] = values

    # Changes all appearances of keyOne or keyTwo in other dictionary entries

    newKeys = adjList.keys()

    for key in newKeys:
        temp = adjList[key]
        adjList[key] = [newIndex if x == keyOne or x == keyTwo else x for x in adjList[key]]

    contractionCount += 1
    return contract(adjList)

def findMinCut(iterations, adjList):
    i = 1
    min_cuts = None

    for i in range(0, int(numIterations(iterations)) + 1):
        print str(i) + " / " + str(numIterations(iterations) + 1) + " : " + str(min_cuts)
        newAdj = deepcopy(adjList)
        if i == 0:
            min_cuts = contract(newAdj)
            continue

        thisMinCut = contract(newAdj)
        if thisMinCut < min_cuts:
            min_cuts = thisMinCut

    return min_cuts




