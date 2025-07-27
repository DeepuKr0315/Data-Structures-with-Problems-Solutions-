# Proble link = https://www.geeksforgeeks.org/problems/remove-loop-in-linked-list/1

def removeLoop(head):
    if head is None or head.next is None:
        return None
    
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            while fast.next != slow:
                fast = fast.next
            fast.next = None
    return head
