# Problem link = https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/description/
# 987. Vertical Order Traversal of a Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
from collections import deque, defaultdict
 
def verticalTraversal(root):
    if not root:
        return []
    
    # Store the nodes along with their positions
    node_list = []
    
    # Queue for BFS: stores node along with its row and column index
    queue = deque([(root, 0, 0)])
    
    while queue:
        node, row, col = queue.popleft()
        if node:
            node_list.append((col, row, node.val))
            queue.append((node.left, row + 1, col - 1))
            queue.append((node.right, row + 1, col + 1))
    
    # Sort the node list by column, row, then value
    node_list.sort()
    
    # Group by column index and extract values
    res = defaultdict(list)
    for col, _, val in node_list:
        res[col].append(val)
    
    # Return sorted columns
    return [res[col] for col in sorted(res)]