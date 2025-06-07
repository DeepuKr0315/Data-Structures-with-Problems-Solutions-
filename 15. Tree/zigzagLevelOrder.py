# problem link = https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
# 103. Binary Tree Zigzag Level Order Traversal
from collections import deque
def zigzagLevelOrder(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    left_to_right = True
    while queue:
        length = len(queue)
        curr_level_values = deque()
        for _ in range(length):
            curr = queue.popleft()
            if left_to_right:
                curr_level_values.append(curr.val)
            else:
                curr_level_values.appendleft(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        result.append(list(curr_level_values))
        left_to_right = not left_to_right
    return result