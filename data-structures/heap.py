class maxHeap:
    def __init__(self, data=None):
        self.data = []
        if data:
            # If there's data, insert the 
            for elem in data:
                self.insert(elem)
                
        # print self.data
        
    def __str__(self):
        return str(self.data)

    # MAIN FUNCTIONS
    def insert(self, element):
        self.data.append(element)
        
        elemIndex = len(self.data) - 1

        parentIndex, parent = self._parent(elemIndex)
        
        while parent < element:
            if parent == None:
                return
            
            self._swap(parentIndex, elemIndex)
            elemIndex = parentIndex

            parentIndex, parent = self._parent(elemIndex)
            
    def extractMax(self):
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
            

if __name__ == "__main__":
    # data = [int(i) for i in open("median.txt").readlines()]

    test = maxHeap([50, 10, 7, 3, 4, 49, 20])

    print test

    print test.extractMax()

    print test
