import heapq

# Making my own MaxHeap implementation because there is no min heap in python
class maxHeap:
    def __init__(self, data=None):
        self.data = []
        if data:
            # If there's data, insert the 
            for elem in data:
                self.heappush(elem)
                
        # print self.data
        
    def __str__(self):
        return str(self.data)

    # MAIN FUNCTIONS
    def heappush(self, element):
        self.data.append(element)
        
        elemIndex = len(self.data) - 1

        parentIndex, parent = self._parent(elemIndex)
        
        while parent < element:
            if parent == None:
                return
            
            self._swap(parentIndex, elemIndex)
            elemIndex = parentIndex

            parentIndex, parent = self._parent(elemIndex)
            
    def heappop(self):
        leaf = self.data.pop()
        maxVal = self.data[0]
        self.data[0] = leaf

        leafIndex = 0
        childIndex, child = self._largestChild(leafIndex)
        
        # End when the leaf is bigger than the largest child
        while leaf < child:
            if child == None:
                return

            self._swap(leafIndex, childIndex)
            
            leafIndex = childIndex
            childIndex, child = self._largestChild(leafIndex)

        return maxVal

    def peek(self):
        if self.len() == 0:
            return None
        
        return self.data[0]
    
    def _largestChild(self, index):
        leftIndex, left = self._leftChild(index)
        rightIndex, right = self._rightChild(index)

        if left < right:
            return (rightIndex, right)
        else:
            return (leftIndex, left)
        

    def _swap(self, index1, index2):
        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]
        
    def _getElement(self, index):
        if index < 0:
            return None
        try:
            return self.data[index]
        except IndexError:
            return None

    # Tree navigation
    
    # Input: Child index, Outputs (Parent Index, Parent)
    def _parent(self, index):
        # If index is even
        if index % 2 == 0:
            parentIndex = index // 2 - 1
            return (parentIndex, self._getElement(parentIndex))
        else:
            parentIndex = index // 2
            return (parentIndex, self._getElement(parentIndex))

    # Both of these: Input = Parent Index, Output = Child Index, Child
    def _leftChild(self, index):
        childIndex = index * 2 + 1
        return (childIndex, self._getElement(childIndex))

    def _rightChild(self, index):
        childIndex = (index + 1) * 2
        return (childIndex, self._getElement(childIndex))

    def len(self):
        return len(self.data)

# Min Heap wrapper
class minHeap:
    def __init__(self, init=[]):
        self.heap = []
        for elem in init:
            self.heappush(elem)

    def __str__(self):
        return str(self.heap)
    
    def heappush(self, item):
        heapq.heappush(self.heap, item)

    def heappop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        if self.len() == 0:
            return None
            
        return self.heap[0]
    
    def len(self):
        return len(self.heap)

class medianMaintenance:
    def __init__(self):
        self.leftHeap = maxHeap()
        self.rightHeap = minHeap()

    def __str__(self):
        return str((str(self.leftHeap), str(self.rightHeap)))

    def insert(self, item):
        leftHeap = self.leftHeap
        rightHeap = self.rightHeap

        leftPeek = leftHeap.peek()

        if item < leftPeek:
            leftHeap.heappush(item)
        else:
            rightHeap.heappush(item)
        leftLen = leftHeap.len()
        rightLen = rightHeap.len()

        delta = leftLen - rightLen
        self._rebalance(delta)

    def median(self):
        leftLen = self.leftHeap.len()
        rightLen = self.rightHeap.len()
        
        delta = leftLen - rightLen

        # If they're completely balanced
        if delta == 0:
            return self.leftHeap.peek()

        # If right heap overflows
        elif delta == -1:
            return self.rightHeap.peek()

        # If left heap overflows
        elif delta == 1:
            return self.leftHeap.peek()

    def _rebalance(self, delta):
        leftHeap = self.leftHeap
        rightHeap = self.rightHeap
        
        # If overflowed right
        if delta <= -2:
            leftHeap.heappush(rightHeap.heappop())

        # If overflowed left
        elif delta >= 2:
            rightHeap.heappush(leftHeap.heappop())

        else:
            return

        # In case the two heaps are super imbalanced:
        # (Currently impossible to reach in this implementation)
        delta = leftHeap.len() - rightHeap.len()
        self._rebalance(delta)

# MM.insert(elem)
# MM.median()
if __name__ == "__main__":
    data = [int(i) for i in open("median.txt").readlines()]

    medianHeap = medianMaintenance()

    _sum = 0
    for num in data:
        medianHeap.insert(num)
        _sum += medianHeap.median()
        print medianHeap
        
    print _sum % 10000        
    
