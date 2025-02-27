# problem link = https://leetcode.com/problems/unique-binary-search-trees-ii/description/
# 95. Unique Binary Search Trees II

def uniqueBST2(n):
    if n == 0:
        return []

    def generate(start, end):
        if start > end:
            return [None]
        tree = []
        for i in range(start, end + 1):
            left_tree = generate(start, i - 1)
            right_tree = generate(i + 1, end)
            for l in left_tree:
                for r in right_tree:
                    current = TreeNode(i)
                    current.left = l
                    current.right = r
                    tree.append(current)
        return tree
    return generate(1, n)