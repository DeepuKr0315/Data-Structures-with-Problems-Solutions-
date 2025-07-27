# Problem link = https://leetcode.com/problems/partition-list/description

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head, x):
    small_head = ListNode(0)
    large_head = ListNode(0)
    small = small_head
    large = large_head
    while head:
        if head.val < x:
            small.next = head
            small = small.next
        else:
            large.next = head
            large = large.next
        head = head.next
    large.next = None
    small.next = large_head.next
    return small_head.next