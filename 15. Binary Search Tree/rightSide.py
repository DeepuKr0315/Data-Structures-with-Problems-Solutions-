from collections import deque
def rightSide(root):
    res = []
    if root is None:
        return []
    queue = deque([root])
    while queue:
        count = 0
        length = len(queue)
        while count < length:
            curr = queue.popleft()
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
            count += 1
            if count == lenght:
                res.append(curr.val)
    return res