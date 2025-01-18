# problem link = https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

def maxProfit(prices):
    left = 0
    profit = 0
    for right in range(1, len(prices)):
        if prices[left] > prices[right]:
            left = right
        else:
            profit = max(profit, prices[right] - prices[left])
    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))