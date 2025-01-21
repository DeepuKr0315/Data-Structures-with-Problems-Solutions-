
# problem link = https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/

def removeDup(head):
    curr = head
    while curr and curr.next != None:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
            continue
        curr = curr.next
    return head

print(removeDup([1,1,2]))