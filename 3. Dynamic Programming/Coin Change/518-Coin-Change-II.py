# Problem link = https://leetcode.com/problems/coin-change-ii/description

def change_recursive(amount, coins):
    cache = {}
    def helper(idx, a):
        if a == amount:
            return 1
        if a > amount or idx == len(coins):
            return 0
        if (idx, a) in cache:
            return cache[(idx, a)]
        cache[(idx, a)] = helper(idx, a + coins[idx]) + helper(idx + 1, a)
        return cache[(idx, a)]
    return helper(0, 0)

def cache_tabulation(amount, coins):
    dp = [[0] * (len(coins) + 1) for i in range(amount + 1)]
    dp[0] = [1] * (len(coins) + 1)
    for a in range(1, amount + 1):
        for idx in range(len(coins) - 1, -1, -1):
            dp[a][idx] = dp[a][idx + 1]
            if a - coins[idx] >= 0:
                dp[a][idx] += dp[a - coins[idx]][idx]
    return dp[amount][0]

print(change_recursive(5, [1, 2, 5]))  # Output: 4
print(cache_tabulation(5, [1, 2, 5]))  # Output: 4