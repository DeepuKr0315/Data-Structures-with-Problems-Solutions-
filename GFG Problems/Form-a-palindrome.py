# Problem link = https://www.geeksforgeeks.org/problems/form-a-palindrome2544/1

def findMinInsertions(s):
    def helper(left, right):
        if left > right:
            return 0
        if left == right:
            return 1
        if s[left] == s[right]:
            return 2 + helper(left + 1, right - 1)
        else:
            return max(helper(left + 1, right), helper(left, right - 1))
    return len(s) - helper(0, len(s) - 1)

# Example usage
s = "abc"
print(findMinInsertions(s))  # Output: 2

def findMinInsertionsMemoization(s):
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
    return len(s) - helper(0, len(s) - 1)

# Example usage
s = "abcd"
print(findMinInsertionsMemoization(s))  # Output: 3

def findMinInsertionsDP(s):
    dp = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s) - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return len(s) - dp[0][len(s) - 1]

# Example usage
s = "abcde"
print(findMinInsertionsDP(s))  # Output: 4