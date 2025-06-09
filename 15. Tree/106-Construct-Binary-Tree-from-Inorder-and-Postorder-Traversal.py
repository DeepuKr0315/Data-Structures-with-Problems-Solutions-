# problem link = https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
# 106. Construct Binary Tree from Inorder and Postorder Traversal

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    def constructBinaryTree(post_start, post_end, in_start, in_end):
        if post_start > post_end or in_start > in_end:
            return None
        root = TreeNode(postorder[post_end])
        index_root = inorder_map[root.val]
        number_of_elements_right = in_end - index_root
        root.left = constructBinaryTree(post_start, post_end - number_of_elements_right - 1, in_start, index_root - 1)
        root.right = constructBinaryTree(post_end - number_of_elements_right, post_end - 1, index_root + 1, in_end)
        return root
    n = len(inorder)
    inorder_map = {}
    for i in range(n):
        inorder_map[inorder[i]] = i
    return constructBinaryTree(0, n-1, 0, n-1)
    