# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Problem Link = https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/?envType=problem-list-v2&envId=binary-tree

def buildTree(preorder, inorder):
    def constructBinaryTree(pre_start,pre_end,in_start,in_end):
        if pre_start>pre_end or in_start>in_end:
            return None
        root = TreeNode(preorder[pre_start])
        index_in  = inorder_map[root.val]
        number_of_elements_left = index_in - in_start
 
        root.left = constructBinaryTree(pre_start + 1, pre_start + number_of_elements_left, in_start, index_in - 1)
 
        root.right = constructBinaryTree(pre_start + number_of_elements_left + 1, pre_end, index_in + 1, in_end)
 
        return root
    n = len(inorder)
    inorder_map = {}
    for i in range(n):
        inorder_map[inorder[i]]=i
    return constructBinaryTree(0, n-1, 0, n-1)