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
    def insertBefore(self, nodeInsert, nodePosition):
        if self.head == nodeInsert and self.tail == nodeInsert:
            return
        self.remove(nodeInsert)
        nodeInsert.prev = nodePosition.prev
        nodeInsert.next = nodePosition

        if nodePosition == self.head:
            self.head = insertNode
        else:
            insertNode.prev.next = insertNode
        nodePosition.prev = insertNode

    def inserPosition(self, position, node):
        curr = self.head
        counter = 0
        while curr != None and counter != position:
            curr = curr.next
            counter += 1
        if curr != None:
            self.insertBefore(curr, Node)
        else:
            if self.head == None:
                self.head = node
                self.tail = node
            else:
                self.remove(node)
                node.next = None
                self.tail.next = node
                self.tail = node