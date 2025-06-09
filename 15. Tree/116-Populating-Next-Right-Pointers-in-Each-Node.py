# Problem Link = https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description

from collections import deque
def connect(self, root):
    if not root:
        return root
    queue = deque([root])
    while(queue):
        count = 0
        length = len(queue)
        prev = None
        while count < length:
            curr = queue.popleft()
            if prev:
                prev.next = curr
            prev = curr
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            count += 1
        curr.next = None
    return root
    