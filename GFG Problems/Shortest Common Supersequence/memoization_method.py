def shortestCommonSupersequence(s1, s2):
    #code here
    memo = {}
    def helper(idx1, idx2):
        if idx1 == len(s1):
            return len(s2) - idx2
        if idx2 == len(s2):
            return len(s1) - idx1
        if (idx1, idx2) in memo:
            return memo[(idx1, idx2)]
        if s1[idx1] == s2[idx2]:
            memo[(idx1, idx2)] = 1 + helper(idx1 + 1, idx2 + 1)
        else:
            memo[(idx1, idx2)] = min(1 + helper(idx1 + 1, idx2), 1 + helper(idx1, idx2 + 1))
        return memo[(idx1, idx2)]
    return helper(0, 0)

# Example usage
s1 = "geek"
s2 = "eke"
print("Length of Shortest Common Supersequence is", shortestCommonSupersequence(s1, s2))
