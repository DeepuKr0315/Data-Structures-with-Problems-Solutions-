# problem link = https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
# 236. Lowest Common Ancestor of a Binary Tree

def lowestCommonAncestor(root, p, q):
    if root is None or root == p or root == q:
        return root
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    if left and right:
        return root
    return left if left else right