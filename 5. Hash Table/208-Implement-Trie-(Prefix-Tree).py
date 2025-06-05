# Problem link = https://leetcode.com/problems/implement-trie-prefix-tree/description

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def isPrefix(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    
trie = Trie()
trie.insert("apple")
trie.insert("bat")

print(trie.search("apple"))
print(trie.search("app"))

trie.insert("app")

print(trie.search("app"))
print(trie.isPrefix("app"))
print(trie.isPrefix("bat"))