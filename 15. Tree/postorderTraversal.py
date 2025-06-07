# 145. Binary Tree Postorder Traversal
# Prolem link = https://leetcode.com/problems/binary-tree-postorder-traversal/description/

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(root):
    stack = [root]
    visited = [False]
    res = []
    while stack:
        curr = stack.pop()
        visit = visited.pop()
        if curr:
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