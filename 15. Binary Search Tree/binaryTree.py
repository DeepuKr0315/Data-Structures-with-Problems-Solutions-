# Design a Binary Search Tree class that supports the following.
#1. Insert a value
#2. Remove a value(should remove first occurance of the value)
#3. Find a value(return the node if the value is found else return False)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        node = Node(value)
        if not self.root:
            self.root = node
            return self
        tree = self.root
        while True:
            if value < tree.value:
                if not tree.left:
                    tree.left = node
                    return self
                tree = tree.left
            else:
                if not tree.right:
                    tree.right = node
                    return self
                tree = tree.right
    def find(self, value):
        if not self.root:
            return False
        tree = self.root
        while tree:
            if value < tree.value:
                tree = tree.left
            elif value > tree.value:
                tree = tree.right
            elif value == tree.value:
                return True
        return False
    def remove(self, value, current=None, parent=None):
        if not self.root:
            return False
        if not current:
            current = self.root
        while current:
            if value < current.value:
                parent = current
                current = current.left
            elif value > current.value:
                parent = current.value
                current = current.right
            else:
                if current.right and current.left:
                    current.value = self.get_min(current.right)
                    self.remove(current.value, current.right, current)
                elif parent is None:
                    if current.right:
                        current.value = current.left.value
                        current.right = current.right.value
                        current.left = current.left.value
                    elif current.left:
                        current.value = current.left.value
                        current.right = current.right.value
                        current.left = current.left.value
                    else:
                        self.root = None
                elif current == parent.left:
                    parent.left = current.left if current.left else current.right
                elif current == parent.right:
                    parent.right = current.left if current.left else current.right
                break
        return self
    def get_min(self):
        while node.left:
            node = node.left
        return node.value
    def inorder_traversal(self, node, result=[]):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        return result
    def preorder_traversal(self, node, result=[]):
        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        return result 
    def postorder_traversal(self, node, result=[]):
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)
        return result

bst = BinarySearchTree()
bst.insert(5).insert(10).insert(2).insert(17).insert(29).insert(23).insert(12)

print("Inorder Traversal: ", bst.inorder_traversal(bst.root, []))
print("Preorder Traversal: ", bst.inorder_traversal(bst.root, []))
print("Postorder Traversal: ", bst.inorder_traversal(bst.root, []))

print("Find 12: ", bst.find(12))
print("Find 15: ", bst.find(15))

bst.remove(12)
print("Inorder traversal after removing 12: ", bst.inorder_traversal(bst.root, []))