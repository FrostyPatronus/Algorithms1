import sys
from random import randint

comparisons = 0
def quicksort(array):
    if len(array) <= 1:
        return array

    
    def swap(i, j):
        array[i], array[j] = array[j], array[i]

    leftLen = 0
    rightLen = 0

    lenArr = len(array)

    global comparisons
    comparisons += lenArr - 1

    # # # CHOOSING THE PIVOT # # #

    ### MEDIAN SORT
    '''first = array[0]
    last = array[lenArr - 1]

    if lenArr % 2 == 0:
        middle = array[(lenArr / 2) - 1]
    else:
        middle = array[lenArr // 2]

    temp = sorted([first, middle, last])
    pivot = temp[1]

    swap(0, array.index(pivot))'''

    ### RANDOMIZED SORT
    pivotInd = randint(0, lenArr - 1)
    pivot = array[pivotInd]
    swap(0, array.index(pivot))

    # / / CHOOSING THE PIVOT / / #

    for i in xrange(1, lenArr):
        if array[i] < pivot:
            if not rightLen:
                leftLen += 1
                continue

            swap(i, leftLen + 1)
            leftLen += 1
        else:
            rightLen += 1

    swap(0, leftLen)

    array[0 : leftLen] = quicksort(array[0 : leftLen])
    array[leftLen + 1 : ] = quicksort(array[leftLen + 1 :])

    return array

'''def main():
    args = map(int, sys.argv[1:])
    quicksort(args)

    print args

if __name__ == "__main__":
    main()'''

file = map(int, open("problemset.txt", "r").readlines())

quicksort(file)

print file == sorted(file)
print comparisons
