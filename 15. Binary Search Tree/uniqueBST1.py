# problem link = https://leetcode.com/problems/unique-binary-search-trees/description/
# 96. Unique Binary Search Trees

def uniqueBST2(n):
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i] = dp[i] + dp[j - 1] * dp[i - j]
    return dp[n]
    