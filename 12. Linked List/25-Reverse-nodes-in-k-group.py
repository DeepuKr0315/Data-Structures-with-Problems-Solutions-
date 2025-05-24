# Problem link = https://leetcode.com/problems/reverse-nodes-in-k-group/?envType=problem-list-v2&envId=linked-list
# 25. Reverse Nodes in k-Group

class ListNode:
    def __init__(self, data = 0, next = None):
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

def reverseKGroups(head, k):
    count = 0
    curr = head
    while(curr is not None and count < k):
        count += 1
        curr = curr.next
    if count == k:
        curr = reverseKGroups(curr, k)
        while(count > 0):
            temp = head.next
            head.next = curr
            curr = head
            head = temp
            count -= 1
        head = curr
    return head

data = [1,2,3,4,5]
k = 3
head = insertIntoLL(data)
head = reverseKGroups(head, k)
printLL(head)