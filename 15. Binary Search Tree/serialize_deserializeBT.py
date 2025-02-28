# problem link = https://leetcode.com/problems/serialize-and-deserialize-bst/description/
# 449. Serialize and Deserialize BST

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.right = None 
        self.left = None

class Codec:
    def serialize(self, root):
        if not root:
            return ""
        result = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("None")
        return result
        
    def deserialize(self, data):
        if not data:
            return None
        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = [root]
        index = 1
        while queue:
            node = queue.pop(0)
            if values[index] != "None":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1
            if values[index] != "None":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1
            if index >= len(values):
                break
        return root