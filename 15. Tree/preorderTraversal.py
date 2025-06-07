def preorderTraversal(root):
    res = []
    stack = [root]
    if root is None:
        return res 
    while stack:
        curr = stack.pop()
        visit = visited.pop()
        if node:
            if visit:
                res.append(curr.val)
            else:
                stack.append(curr)
                visited.append(True)
                stack.append(curr.right.val)
                visited.append(False)
                stack.append(curr.left.val)
                visited.append(False)
    return res