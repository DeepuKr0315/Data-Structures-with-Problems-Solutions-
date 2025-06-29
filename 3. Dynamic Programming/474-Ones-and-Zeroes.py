# Problem link = https://leetcode.com/problems/ones-and-zeroes/description

def findMaxForm(strs, m, n):
    memo = {}
    def helper(idx, m, n):
        if idx == len(strs):
            return 0
        if (idx, m, n) in memo:
            return [(idx, m, n)]
        zero_count = strs[idx].count('0')
        one_count = strs[idx].count('1')
        exclude = helper(idx + 1, m, n)
        include = 0
        if m >= zero_count and n >= one_count:
            include = 1 + helper(idx + 1, m - zero_count, n - one_count)
        memo[(idx, m, n)] = max(include, exclude)
        return memo[(idx, m, n)]
    return helper(0, m, n)

def findMaxForm_dp(strs, m, n):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for s in strs:
        zero_count = s.count('0')
        one_count = s.count('1')
        for i in range(m, zero_count - 1, -1):
            for j in range(n, one_count - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - zero_count][j - one_count] + 1)
    return dp[m][n]

# Example usage
strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(findMaxForm(strs, m, n))  # Output: 4
print(findMaxForm_dp(strs, m, n))  # Output: 4