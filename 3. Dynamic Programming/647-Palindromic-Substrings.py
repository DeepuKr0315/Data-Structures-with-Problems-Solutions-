
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

def countPalindrome_aproach2(s):
    n = len(s)
    dp = [[0]*(n) for _ in range(n)]
    result = 0
    for l in range(1, n+1):
        for i in range(n-l+1):
            j = i+l-1
            if i == j:
                dp[i][j] = True
                result += 1
            elif s[i] == s[j] and (j == i+1 or dp[i+1][j-1]):
                dp[i][j] = True
                result += 1
            else:
                dp[i][j] = False
    return result

s = "abc"
print(countPalindrome(s))

s = "abc"
print(countPalindrome_aproach2(s))