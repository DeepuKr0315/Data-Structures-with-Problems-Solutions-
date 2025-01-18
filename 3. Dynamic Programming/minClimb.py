def minCost(cost):
    n = len(cost)
    def helper(index):
        if index > n:
            return 0
        oneStep = cost[index] + helper(index+1)
        twoStep = cost[index] + helper(index+2)
        return min(oneStep. twoStep)
    return min(helper(0), helper(1))

