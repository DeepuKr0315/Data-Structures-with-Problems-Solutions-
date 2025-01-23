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
        if self.tail == node:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next = None
        nod.prev = None

    def insertNode(self, nodePosition, nodeInsert):
        if self.head == nodeInsert and self.tail == nodeInsert:
            return
        # remove node if it is in the DLL
        self.remove(nodeInsert)
        nodeInsert.prev = nodePosition.prev
        nodeInsert.next = nodePosition
        if nodePosition == self.head:
            self.head = nodeInsert
        else:
            nodeInsert.prev.next = nodeInsert
        nodePosition.prev = nodeInsert