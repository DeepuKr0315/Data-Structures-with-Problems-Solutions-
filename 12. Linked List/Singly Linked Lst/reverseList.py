
# problem link = https://leetcode.com/problems/reverse-linked-list/description/

def reverseList(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev