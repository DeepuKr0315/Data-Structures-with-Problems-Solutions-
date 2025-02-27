# problem link = https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# 235. Lowest Common Ancestor of a Binary Search Tree

def lowestCommonAncestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.val
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
    return None