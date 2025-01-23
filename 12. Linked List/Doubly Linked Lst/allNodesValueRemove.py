# 1. Remove all the nodes in the doubly linked list which have their value equal to a given value
# 2. Insert  node at a desired position(node and position are given). The linked list is 0 indexed.
# If given node is existng in the linked list shift it to the desired position

# [1, 2, 2, 3, 2, 2] ==> remove 2 ==> [1, 3] will be our output

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None
def linkNodes(node1, node2):
    node1.next = node2
    node2.prev = node1

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def remove(self, node):
        if self.head == node:
            self.head = node.next
        if sel.tail == node:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next = None
        node.prev = None
    def insert(self, nodeInsert, nodePosition):
        if self.head == nodeInsert and self.tail == nodeInsert:
            return
        self.remove(nodeInsert)
        nodeInsert.prev = nodePosition.prev
        nodeInsert.next = nodePosition
        if nodePosition == self.head:
            self.head = nodeInsert
        else:
            nodeInsert.prev.next = nodeInsert
        nodePosition.prev = nodeInsert
    def allNodesValueRemove(self, value):
        curr = self.head
        while curr:
            temp = curr
            curr = curr.next
            if temp.val == value:
                self.remove(temp)