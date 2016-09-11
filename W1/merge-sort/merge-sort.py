# takes two sorted lists of numbers and produces a list that combines them that is sorted. 
# The merge part in merge sort
def merge(one, two):
    array = []
    i = j = 0

    one.reverse()
    two.reverse()
    while one and two:
        s = one if one[-1] <= two[-1] else two
        array.append(s.pop())

    extra = one if one else two
    extra.reverse()

    array.extend(extra)

    return array

def merge_sort(array):
    array_len = len(array)

    if array_len <= 1:
        return array

    array_1 = array[0 : array_len // 2]
    array_2 = array[array_len // 2 : ]

    return merge(merge_sort(array_1), merge_sort(array_2))
