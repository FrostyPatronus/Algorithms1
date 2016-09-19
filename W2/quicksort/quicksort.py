import sys
from random import randint

def quicksort(array):

    if not array:
        return []

    def swap(i, j):
        array[i], array[j] = array[j], array[i]

    leftLen = 0
    rightLen = 0

    lenArr = len(array)

    pivotInd = randint(0, lenArr - 1)
    pivot = array[pivotInd]

    swap(0, pivotInd)

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

def main():
    args = map(int, sys.argv[1:])
    quicksort(args)

    print args

if __name__ == "__main__":
    main()