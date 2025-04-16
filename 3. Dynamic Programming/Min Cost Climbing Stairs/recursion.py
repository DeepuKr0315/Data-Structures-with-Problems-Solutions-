# Problem link = https://leetcode.com/problems/min-cost-climbing-stairs/description/?envType=study-plan-v2&envId=dynamic-programming
# 746. Min Cost Climbing Stairs


def minCostClimbingStairs(cost):
    n = len(cost)
    def helper(index):
        if index >= n:
            return 0
        oneStep = cost[index] + helper(index+1)
        twoStep = cost[index] + helper(index+2)
        return min(oneStep,  twoStep)
    return min(helper(0), helper(1))

cost = [10,15,20]
print(minCostClimbingStairs(cost))