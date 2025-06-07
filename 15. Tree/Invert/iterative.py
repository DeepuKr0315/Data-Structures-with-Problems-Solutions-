# problem link = https://leetcode.com/problems/invert-binary-tree/description/
# 226. Invert Binary Tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
def invertIterative(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        curr = queue.popleft()
        curr.left, curr.right = curr.right, curr.left
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)
    return root