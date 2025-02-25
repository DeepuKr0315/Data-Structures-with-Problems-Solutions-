# problem link = https://leetcode.com/problems/invert-binary-tree/description/
# 226. Invert Binary Tree

def invertRecursive(node):
    if not node:
        return
    temp = node.left
    node.left = node.right
    node.right = temp
    invertRecursive(node.left)
    invertRecursive(node.right)
    return node