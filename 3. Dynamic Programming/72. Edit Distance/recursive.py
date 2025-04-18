# Problem link == https://leetcode.com/problems/edit-distance/description/

def minDistance(word1, word2):
    n = len(word1)
    m = len(word2)
    def helper(index1, index2):
        if index1 > n-1 and index2 > m-1:
            return 0
        if index1 > n-1:
            return m - index2
        if index2 > m-1:
            return n - index1
        if word1[index1] == word2[index2]:
            return helper(index1 + 1, index2 + 1)
        replace = 1 + helper(index1 + 1, index2 + 1)
        delete = 1 + helper(index1 + 1, index2)
        insert = 1 + helper(index1, index2 + 1)
        return min(replace, delete, insert)
    return helper(0, 0)
word1 = "dinitrophenylhydrazine"
word2 = "acetylphenylhydrazine"
print(minDistance(word1, word2))