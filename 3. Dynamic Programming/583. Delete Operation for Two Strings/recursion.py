# Problem link ==> https://leetcode.com/problems/delete-operation-for-two-strings/description/
def minDistance(word1, word2):
    def helper(idx1, idx2):
        if idx1 == len(word1) or idx2 == len(word2):
            return 0
        if word1[idx1] == word2[idx2]:
            return 1 + helper(idx1 + 1, idx2 + 1)
        return max(helper(idx1 + 1, idx2), helper(idx1, idx2 + 1))
    return len(word1) + len(word2) - 2 * helper(0, 0)

# Example usage
word1 = "sea"
word2 = "eat"
print(minDistance(word1, word2))  # Output: 2