# Problem Link = https://leetcode.com/problems/binary-tree-paths/description

def binaryTreePaath(root):
    result = []
    def dfs(node, path):
        if not node:
            return
        if path:
            path += "->" + str(node.val)
        else:
            path = str(node.val)
        if not node.left and not node.right:
            result.append(path)
            return
        dfs(node.left, path)
        dfs(node.right, path)
    dfs(root, "")
    return result