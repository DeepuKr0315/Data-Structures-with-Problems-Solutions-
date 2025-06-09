# Problem Link = https://leetcode.com/problems/diameter-of-binary-tree/description/
# 543. Diameter of Binary Tree

def diameterBinaryTree(root):
    if not root:
        return 0
    maxDiameter = 0
    def dfs(node):
        nonlocal maxDiameter
        if not node:
            return -1
        leftHeight = dfs(node.left)
        rightHeight = dfs(node.right)
        diameter = leftHeight + rightHeight + 2
        maxDiameter = max(maxDiameter, diameter)
        return max(leftHeight, rightHeight) + 1
    dfs(root)
    return maxDiameter