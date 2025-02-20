# problem link = https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
# 107. Binary Tree Level Order Traversal II

from collections import deque

def levelOrder2(root):
    if root is None:
        return []
    result = []    
    queue = deque([root])
    while queue:
        length = len(queue)
        curr_level_values = []
        for _ in range(length):
            curr = queue.popleft()
            curr_level_values.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        result.append(curr_level_values)
    return result[::-1]

