from collections import deque
def leftSide(root):
    if root is None:
        return []
    res = []
    queue = deque([root])
    while queue:
        count = 0
        length = len(queue)
        while count < length:
            count += 1
            curr = queue.popleft()
            if count == 1:
                res.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            
    return res