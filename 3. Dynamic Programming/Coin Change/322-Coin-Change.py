# Problem link = https://leetcode.com/problems/coin-change/description/

def coinChange(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[amount] if dp[amount] != amount + 1 else -1

coins = [1,2,5]
amount = 11
print(coinChange(coins, amount))