class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    def addAtBeginning(self, value):
        node = Node(value)
        if not self.first:
            self.first = node
            self.last = node
        else:
            temp = self.first
            self.first = node
            self.first.next = temp
        self.szie += 1
        return self
    def removeAtBeginning(self):
        if not self.first:
            return None
        temp = self.first
        self.first = self.first.next
        self.size -= 1
        if self.size == 0:
            self.last = None
        return temp.value