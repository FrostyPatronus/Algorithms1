import sys

def quicksort(array):
    if not array:
        return []

    pivot = array[0]

    left = []
    right = []
    for i in array[1 :]:
        if i < pivot:
            left.append(i)
        else:
            right.append(i)

    left = quicksort(left)
    right = quicksort(right)

    left.append(pivot)
    return left + right

def main():
    args = map(int, sys.argv[1:])
    print quicksort(args)


if __name__ == "__main__":
    main()