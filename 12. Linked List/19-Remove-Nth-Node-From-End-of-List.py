# 19. Remove Nth Node From End of List
# problem link = https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=problem-list-v2&envId=linked-list
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head
    while n > 0 and right:
        right = right.next
        n -= 1
    while right:
        right = right.next
        left = left.next

    left.next = left.next.next
    return dummy.next

print(removeNthFromEnd(head = [1,2,3,4,5], n = 2))