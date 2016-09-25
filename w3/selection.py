# HOW TO USE:
# python selection <numbers separated by spaces> <ith degree statistic>

import sys
import random

def partition(array):
    def swap(i, j):
        array[i], array[j] = array[j], array[i]

    # SELECTING PIVOT
    pivotIndex = random.randrange(0, len(array))
    pivot = array[pivotIndex]

    swap(pivotIndex, 0)

    left = []
    right = []

    for elem in array[1 :]:
        left.append(elem) if elem < pivot else right.append(elem)

    return [left, pivot,right]
    

def select(array, stat):
    if len(array) == 1:
        return array[0]

    newArray = array[:]
    temp = partition(newArray)

    left = temp[0]
    pivot = temp[1]
    right = temp[2]

    # DISCRIMINANT
    lenLeft = len(left)
    disc = stat - lenLeft - 1

    # print disc
    # print pivot

    if disc < 0:
        return select (left, stat)
    elif disc == 0:
        return pivot
    else:
        return select (right, disc)

def main():
    args = sys.argv[1 : ]

    array = map(int, args[ : -1])
    stat = int(args[-1])

    print "ARRAY:", array
    print "STATISTIC:", stat

    print str(stat) + "th degree statistic:", select(array, stat)

if __name__ == "__main__":
    main()