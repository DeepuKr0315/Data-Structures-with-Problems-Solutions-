"""
Time complexity:

enqueue: O(logn)

dequeue: O(logn)

Space complexity: O(1)
"""
class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority

class PriorityQueue:
    def __init__(self):
        self.data = []
    
    def enqueue(self, value, priority):
        node = Node(value, priority)
        self.data.append(node)
        self.bubble_up(node)
        return self
    
    def bubble_up(self):
        index = (self.data) - 1
        element = self.data[index]
        while index > 0:
            parent_index = (index - 1) // 2
            parent = self.data[parent_index]
            if element.priority > parent.priority:
                break
            self.data[index] = parent
            self.data[parent_index] = element
            index = parent_index

    def dequeue(self):
        min_element = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self.bubble_down()
        return min_element

    def bubble_down(self):
        index = 0
        length = len(self.data)
        element = self.data[0]
        while True:
            left_child_idx = 2 * index + 1
            right_child_idx = 2 * index + 2
            left_child, right_child = None, None
            smallest = None
            if left_child_idx < length:
                left_child = self.data[left_child_idx]
                if left_child.priority < element.priority:
                    smallest = left_child_idx
            if right_child_idx < length:
                right_child = self.data[right_child_idx]
                if (smallest is None and right_child.priority < left_child.priority) or (smallest is not None and right_child.priority < left_child.priority):
                    smallest = right_child_idx
            if smallest is None:
                break
            self.data[index] = self.data[smallest]
            self.data[smallest] = element
            index = smallest
            