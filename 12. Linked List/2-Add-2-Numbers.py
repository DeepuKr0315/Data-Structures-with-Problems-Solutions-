
# problem link = https://leetcode.com/problems/add-two-numbers/description/

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addNumbers(l1, l2):
    results = ListNode()
    current = results
    carryForward = 0
    while l1 or l2 or carryForward:
        l1Value = l1.value if l1 else 0
        l2Value = l2.value if l2 else 0
        sum = l1Value + l2Value + carryForward
        nodeValue = sum % 10
        carryForward = sum // 10
        current.next = ListNode(nodeValue)
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return results.next

print(addNumbers(l1 = [2,4,3], l2 = [5,6,4]))