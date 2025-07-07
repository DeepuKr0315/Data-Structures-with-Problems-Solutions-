# Problem link = https://www.geeksforgeeks.org/dsa/longest-repeated-subsequence/

def longest_repeated_subsequence(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == s[j - 1] and i != j:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][n]

s = "aabb"
print(longest_repeated_subsequence(s))  # Output: 2

# How to print the subsequence? 
def print_longest_repeated_subsequence(s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[j - 1] == s[i - 1] and i != j:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    i, j = n, n
    lrs = []
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j - 1] + 1:
            lrs.append(s[i - 1])
            i -= 1
            j -= 1
        elif dp[i][j] == dp[i - 1][j]:
            i -= 1
        else:
            j -= 1
    ''.join(reversed(lrs))
    return ''.join(reversed(lrs))

s = 'AABEBCDD'
print(print_longest_repeated_subsequence(s))  # Output: ABD