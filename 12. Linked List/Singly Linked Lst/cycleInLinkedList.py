
# problem link = https://leetcode.com/problems/linked-list-cycle/description/

def openLoop(head):
    if not head or not head.next:
        return False
    tortoise = head
    hare = head
    while hare and hare.next:
        hare = hare.next.next
        tortoise = tortoise.next
        if hare == tortoise:
            return True
    return False
    # To find positon
    position = head
    while position != tortoise:
        position = position.next
        tortoise = tortoise.next
    return tortoise