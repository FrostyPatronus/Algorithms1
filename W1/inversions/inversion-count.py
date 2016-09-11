# takes two sorted lists of numbers and produces a list that combines them that is sorted. 
# The merge part in merge sort
file = open("text")
content = file.readlines()
content = [int(c) for c in content] 

c = 0
def merge(one, two):
    global c
    array = []
    i = j = 0

    one.reverse()
    two.reverse()
    while one and two:
        s = None
        if one[-1] <= two[-1]:
            s = one
        else:
            s = two
            c += len(one)

        array.append(s.pop())

    extra = None
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

print merge_sort(content)
print c