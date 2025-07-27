# Problem link = https://www.geeksforgeeks.org/problems/rotate-a-linked-list/1

def rotate_linked_list(head, k):
    if head is None or k <= 0:
        return head
    curr = head
    for _ in range(k):
        while curr.next:
            curr = curr.next
        curr.next = head
        curr = curr.next
        head = head.next
        curr.next = None
    return head
