def minDistance(word1, word2):
    memo = {}
    def helper(idx1, idx2):
        if idx1 == len(word1) or idx2 == len(word2):
            return 0
        if (idx1, idx2) in memo:
            return memo[(idx1, idx2)]
        if word1[idx1] == word2[idx2]:
            memo[(idx1, idx2)] = 1 + helper(idx1 + 1, idx2 + 1)
        else:
            memo[(idx1, idx2)] = max(helper(idx1 + 1, idx2), helper(idx1, idx2 + 1))
        return memo[(idx1, idx2)]
    
    return len(word1) + len(word2) - 2 * helper(0, 0)
# Example usage
word1 = "mart"
word2 = "karma"
print(minDistance(word1, word2))  # Output: 3