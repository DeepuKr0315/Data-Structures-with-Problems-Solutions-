
# Problem link ==> https://leetcode.com/problems/longest-palindromic-subsequence/description/

def longestPalindromicSubsequenceRecursive(s):
    def helper(left, right):
        if left > right:
            return 0
        if left == right:
            return 1
        if s[left] == s[right]:
            return 2 + helper(left + 1, right - 1)
        else:
            return max(helper(left + 1, right), helper(left, right - 1))
    return helper(0, len(s) - 1)

def longestPalindromicSubsequenceMemoization(s):
    memo = {}
    
    def helper(left, right):
        if left > right:
            return 0
        if left == right:
            return 1
        if (left, right) in memo:
            return memo[(left, right)]
        if s[left] == s[right]:
            memo[(left, right)] = 2 + helper(left + 1, right - 1)
        else:
            memo[(left, right)] = max(helper(left + 1, right), helper(left, right - 1))
        return memo[(left, right)]
    return helper(0, len(s) - 1)

def longestPalindromicSubsequence(s):
    n = len(s)
    dp = [[0]*n for _ in range(n)]
    for l in range(1, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if i == j:
                dp[i][j] = 1
            elif s[i] == s[j]:
                dp[i][j] = 2 + dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]

def longestPalindromicSpaceOptimization(s):
    curr = [0] * len(s)
    prev = [0] * len(s)
    for i in range(len(s) - 1, -1, -1):
        curr[i] = 1
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                curr[j] = 2 + prev[j - 1]
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr[:]
    return curr[-1]

s = "abcbd"
print(longestPalindromicSubsequenceRecursive(s))  # Output: 3
print(longestPalindromicSubsequenceMemoization(s))  # Output: 3
print(longestPalindromicSpaceOptimization(s))  # Output: 3
print(longestPalindromicSubsequence(s))  # Output: 3