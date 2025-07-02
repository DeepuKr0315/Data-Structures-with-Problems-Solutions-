
# problem link ==> https://leetcode.com/problems/palindromic-substrings/description/

def countPalindrome(s):
    n = len(s)
    dp = [[-1]*n for _ in range(n)]

    def helper(i, j):
        if i == j:
            dp[i][j] = True
            return dp[i][j]
        if i > j:  # An empty substring is also considered a palindrome
            return True
        if dp[i][j] != -1:
            return dp[i][j]
        if s[i] == s[j] and (j == i+1 or helper(i+1, j-1)):
            dp[i][j] = True
        else:
            dp[i][j] = False
        return dp[i][j]

    res = 0
    for i in range(n):
        for j in range(i, n):
            if helper(i, j):
                res += 1

    return res

s = "abc"
print(countPalindrome(s))