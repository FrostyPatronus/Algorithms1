# @author Timothy Samson

class HashTable:

    def __init__(self):
        pass

    def hashFunction(self):
        pass
    
    def insert(self):
        pass
    
    def delete(self):
        pass

    def lookUp(self):
        pass

# def main(data):
#     count = 0
#     index = 0

#     answers = {}
    
#     for num1 in data:
#         for target in range (-10000, 10000 + 1):
#             num2 = target - num1
#             if data.has_key(num2):
#                 if num2 == num1:
#                     continue

#                 if answers.has_key(target):
#                     continue
                
#                 count += 1
#         print index
#         index += 1
#     print count        

# {Int:None}, TargetSum -> Boolean

count = 0
MIN = -10000
MAX = 10001


# Naive implementation
def twoSum(data, target):
    global count
    for num1 in data:
        num2 = target - num1
        
        if data.has_key(num2):
            if num2 == num1:
                continue
            
            count += 1
            return (num1, num2)
    
    return False

def main(data):
    for target in range(MIN, MAX):
        print target, count, twoSum(data, target)
        
# Implementation with bisect
import bisect
def twoSumBisect(array):
    out = set()
    for i in array:
        lower = bisect.bisect_left(array, -10000 - i)
        upper = bisect.bisect_right(array, 10000 - i)
        out = out | set([i + j for j in array[lower:upper]])
    return out

if __name__ == "__main__":
    dataList =  [int(i) for i in open("2sum.txt", "r").readlines()]
    dataList.sort()
    # data = {i : None for i in dataList}

    # dataList.sort()
    # dataList = dataList[: len(dataList) // 2 + 1]
    
    # print dataList
    # print data
    
    print len(twoSumBisect(dataList))
