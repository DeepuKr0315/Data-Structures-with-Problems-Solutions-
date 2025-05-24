class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

def insertIntoLL(data):
    if not data:
        return None
    head = ListNode(data[0])
    curr = head
    for value in data[1:]:
        curr.next = ListNode(value)
        curr = curr.next
    return head

def printLL(head):
    while head:
        print(head.data, " -> ", end="")
        head = head.next
    print("None")

def removeDuplicatesII(head):
    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy
    while head:
        if head.next and head.data == head.next.data:
            while head.next and head.data == head.next.data:
                head = head.next
            prev.next = head.next
        else:
            prev = prev.next
        head = head.next
    return dummy.next


data = [1,2,3,3,4,4,5]
head = insertIntoLL(data)
head = removeDuplicatesII(head)
printLL(head)