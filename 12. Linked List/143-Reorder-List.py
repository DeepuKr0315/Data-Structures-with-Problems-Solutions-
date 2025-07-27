# Problem link = https://leetcode.com/problems/reorder-list/description

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    if not head or head.next is None:
        return head
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    first = head
    second = prev
    while second.next:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2
    return head

