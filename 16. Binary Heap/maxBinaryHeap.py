class MaxBinaryHeap:
    def __init__(self):
        self.heap = []
    
    def buildHeap(self, array):
        length = len(array)
        last_parent_index = length // 2 - 1
        for i in range(last_parent_index, -1, -1):
            self.bubbleDown(array, i)
        self.heap = array
        return self

    def bubbleDown(self, array, index):
        length = len(array)
        current = array[index]
        while True:
            left_child_idx = 2 * index + 1
            right_child_idx = 2 * index + 2
            largest = None
            if left_child_idx < length:
                left_child = array[left_child_idx]
                # If it's larger than current element, it could be the largest
                if left_child > current:
                    largest = left_child_idx
            if right_child_idx < length:
                right_child = array[right_child_idx]
                # If right child is larger than current and left child, it's the largest
                if (largest is None and right_child > current) or (largest is not None and right_child > array[largest]):
                    largest = right_child_idx
            if largest is None:
                break
            else:
                array[index], array[largest] = array[largest], array[index]
                index = largest
            
    def extractMax(self):
        maxValue = self.heap[0]
        last = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last
            self.bubbleDown(self.heap, 0)
        return maxValue

    def insert(self, value):
        self.heap.append(value)
        self.bubbleUp()
        return self
    
    def bubbleUp(self):
        index = len(self.heap) - 1
        value = self.heap[index]
        while index > 0:
            parent_index = (index - 1) // 2
            parent_value = self.heap[parent_index]
            if value <= parent_value:
                break
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            index = parent_index
    
    def peek(self):
        return self.heap[0]

heap = MaxBinaryHeap()
heap.buildHeap([4, 7, 3, 0, 9, 3, 2, 6])
print(heap.heap)
print(heap.peek())
print(heap.extractMax())