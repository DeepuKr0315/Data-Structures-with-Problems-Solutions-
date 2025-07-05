# Problem link = https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

def maxProfit(prices):
    memo = {}
    # 0 = buy, 1 = sell, 2 = cooldown
    def helper(idx, can_buy):
        if idx >= len(prices):
            return 0
        if (idx, can_buy) in memo:
            return memo[(idx, can_buy)]
        if can_buy == 0:
            buy = helper(idx + 1, 1) - prices[idx]
            hold = helper(idx + 1, can_buy)
            memo[(idx, can_buy)] = max(buy, hold)
        elif can_buy == 1:
            sell = helper(idx + 1, 2) + prices[idx]
            hold = helper(idx + 1, can_buy)
            memo[(idx, can_buy)] = max(sell, hold)
        else:
            memo[(idx, can_buy)] = helper(idx + 1, 0)  # Cooldown state
        return memo[(idx, can_buy)]
    return helper(0, 0)

def maxProfitTabulation(prices):
    dp = [[0] * 3 for _ in range(len(prices) + 1)]
    for i in range(len(prices) - 1, -1, -1):
        for j in range(3):
            if j == 0:
                dp[i][j] = max(dp[i + 1][1] - prices[i], dp[i + 1][j])
            elif j == 1:
                dp[i][j] = max(dp[i + 1][2] + prices[i], dp[i + 1][j])
            else:
                dp[i][j] = dp[i + 1][0]
    return dp[0][0]

# Example usage
prices = [1, 2, 3, 0, 2]
print(maxProfit(prices))  # Output: 3
print(maxProfitTabulation(prices))  # Output: 3