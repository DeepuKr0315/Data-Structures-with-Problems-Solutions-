# Problem link = https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=study-plan-v2&envId=dynamic-programming
# 746. Min Cost Climbing Stairs

def minClimbStairs(cost):
    dp = [0] * (len(cost) + 1)
    dp[0], dp[1] = 0, 0
    for i in range(2, len(cost) + 1):
        oneStep = cost[i - 1] + dp[i - 1]
        twoStep = cost[i - 2] + dp[i - 2]
        dp[i] = min(oneStep, twoStep)
    return dp[-1]
cost = [10,15,20]
print(minClimbStairs(cost))