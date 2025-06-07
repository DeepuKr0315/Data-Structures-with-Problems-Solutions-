# problem link = https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# 108. Convert Sorted Array to Binary Search Tree

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    def helper(nums, left, right):
        if not right:
            right = len(nums) - 1
        if left > right:
            return
        middle = (right + left) // 2
        node = TreeNode(middle)
        node.left = helper(nums, left, mid - 1)
        node.right = helper(nums, mid + 1, right)
        return node
    return helper(nums, 0, None)