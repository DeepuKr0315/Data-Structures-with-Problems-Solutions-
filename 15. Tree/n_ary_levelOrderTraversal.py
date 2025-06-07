# proble link = https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
# 429. N-ary Tree Level Order Traversal

from collections import deque

class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def levelOrder(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        length = len(queue)
        curr_level = []
        for _ in range(length):
            node = queue.popleft()
            curr_level.append(node.val)
            queue.extend(node.children)
        result.append(curr_level)
    return result