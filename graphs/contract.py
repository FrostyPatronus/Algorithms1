from random import randint

contractionCount = 1

def contract(adjList):
    global contractionCount

    keys = adjList.keys()
    len_keys = len(keys)

    index1 = randint(0, len_keys - 1)
    index2 = randint(0, len_keys - 1)

    while index2 == index1:
        index2 = randint(0, len_keys - 1)

    print "index 1:", index1
    print "index 2:", index2

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
