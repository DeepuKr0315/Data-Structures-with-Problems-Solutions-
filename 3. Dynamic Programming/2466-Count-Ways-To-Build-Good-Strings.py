# Problem link = https://leetcode.com/problems/count-ways-to-build-good-strings/description/

def countGoodStrings(low, high, zero, one):
    MOD = 10 ** 9 + 7
    dp = {}
    def helper(length):
        if length > high:
            return 0
        if length in dp:
            return dp[length]
        dp[length] = 1 if length >= low else 0
        dp[length] += helper(length + zero) + helper(length + one)
        return dp[length] % MOD
    return helper(0)

def countGoodStrings_approach2(low, high, zero, one):
    dp = { 0: 1 }
    MOD = 10 ** 9 + 7
    for i in range(1, high + 1):
        dp[i] = (dp.get(i - zero, 0) + dp.get(i - 1, 0)) % MOD
    return sum(dp[i] for i in range(low, high + 1)) % MOD
# Example usage
print(countGoodStrings(low = 3, high = 3, zero = 1, one = 1))  # Output: 8
print(countGoodStrings_approach2(low = 3, high = 3, zero = 1, one = 1))  # Output: 8