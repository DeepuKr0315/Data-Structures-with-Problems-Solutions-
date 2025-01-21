
# problem link = https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

def removeDup(head):
    curr = head
    while curr:
        nextDistinct = curr.next
        while nextDistinct is not None and curr.val == nextDistinct.val:
            nextDistinct = nextDistinct.next
        curr.next = nextDistinct
        curr = nextDistinct
    return head

print(removeDup([1,1,2]))