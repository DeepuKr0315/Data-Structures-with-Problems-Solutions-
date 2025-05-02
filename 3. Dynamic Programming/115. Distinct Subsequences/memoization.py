# Problem link = https://leetcode.com/problems/distinct-subsequences/description/
# 115. Distinct Subsequences

def numDistinct(s, t):
    cache = {}
    def helper(i, j):
        if j == len(t):
            return 1
        if i == len(s):
            return 0
        if s[i] == t[j]:
            cache[(i, j)] = helper(i + 1, j + 1) + helper(i + 1, j)
        else:
            cache[(i, j)] = helper(i + 1, j)
        return cache[(i, j)]
    return helper(0, 0)

s = "rabbbit"
t = "rabbit"
print(numDistinct(s, t))